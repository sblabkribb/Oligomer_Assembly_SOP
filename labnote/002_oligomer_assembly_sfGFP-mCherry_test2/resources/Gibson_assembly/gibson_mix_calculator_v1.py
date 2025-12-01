from pathlib import Path
import pandas as pd
import os

# --- 계산 유틸 ---
def pmol_per_ul(conc_ng_ul: float, bp: int) -> float:
    """ng/µL와 bp로부터 pmol/µL 계산 (pmol = ng*1000 / (bp*650))"""
    return (conc_ng_ul * 1000.0) / (bp * 650.0)

def round_to(x: float, step: float) -> float:
    """피펫 가능한 단위로 반올림 (예: 0.1 µL)"""
    return round(x / step) * step if step and step > 0 else x

def _strip_quotes(path_str: str) -> str:
    """양끝 따옴표(큰/작은) 제거"""
    return str(path_str).strip().strip('"').strip("'")

# --- 메인 함수 ---
def run_ratio_mode_fixed(
    input_path: str,
    output_path: str,
    vector_length_bp: int,
    vector_conc_ng_ul: float,
    dna_mix_total_ul: float,
    insert_to_vector_molar: float,
    round_unit_ul: float = 0.1,
):
    """
    Gibson Assembly용 부피 및 몰수 계산기
    Output: Output + Issues 시트만 저장
    """
    # 경로 방어: 따옴표가 붙거나 공백이 있어도 OK
    input_path = _strip_quotes(input_path)
    output_path = _strip_quotes(output_path)

    in_path = Path(input_path)
    if not in_path.exists():
        raise FileNotFoundError(f"입력 파일이 없습니다: {in_path}")

    # 입력 읽기
    if in_path.suffix.lower() in (".xlsx", ".xls"):
        df_in = pd.read_excel(in_path)
    else:
        df_in = pd.read_csv(in_path)

    # 헤더 표준화 (공백/대소/µL↔uL 혼용 보정)
    cols = [c.strip() for c in df_in.columns]
    cols = [c.replace("uL", "µL").replace("Ul", "µL").replace("UL", "µL") for c in cols]
    df_in.columns = cols

    # 필수 컬럼 검증
    required_cols = ["Position", "Name", "insert_length (bp)", "insert_conc. (ng/µL)"]
    missing = [c for c in required_cols if c not in df_in.columns]
    if missing:
        raise ValueError(f"필수 컬럼이 없습니다: {missing}\n현재 컬럼: {list(df_in.columns)}")

    # 벡터 몰농도 (pmol/µL)
    Cv = pmol_per_ul(vector_conc_ng_ul, vector_length_bp)

    records, issues = [], []

    for i, row in df_in.iterrows():
        pos = row.get("Position", None)
        name = row.get("Name", None)

        try:
            insert_len = float(row["insert_length (bp)"])
            insert_conc = float(row["insert_conc. (ng/µL)"])
        except Exception as e:
            issues.append({
                "Row": i + 2,
                "Position": pos,
                "Name": name,
                "Reason": f"값 변환 실패: {e}",
            })
            continue

        Ci = pmol_per_ul(insert_conc, insert_len)

        if Cv <= 0 or Ci <= 0:
            issues.append({
                "Row": i + 2,
                "Position": pos,
                "Name": name,
                "Reason": f"잘못된 농도/길이 (Cv={Cv:.3g}, Ci={Ci:.3g})",
            })
            continue

        # 목표 몰비로 부피 계산 (벡터/인서트 농도 차 반영)
        ratio = float(insert_to_vector_molar)  # insert : vector
        v_vec = dna_mix_total_ul / (1.0 + (ratio * (Cv / Ci)))
        v_ins = dna_mix_total_ul - v_vec

        v_vec_r = round_to(v_vec, round_unit_ul)
        v_ins_r = round_to(v_ins, round_unit_ul)

        vec_pmol = Cv * v_vec_r
        ins_pmol = Ci * v_ins_r

        records.append({
            "Position": pos,
            "Name": name,
            "insert_length (bp)": insert_len,
            "insert_conc. (ng/µL)": insert_conc,
            "insert_vol. (µL)": v_ins_r,
            "vector_vol. (µL)": v_vec_r,
            "insert_mol (pmols)": round(ins_pmol, 3),
            "vector_mol (pmols)": round(vec_pmol, 3),
            "total_mol (pmols)": round(ins_pmol + vec_pmol, 3),
        })

    df_out = pd.DataFrame(records)
    df_issues = pd.DataFrame(issues)

    # --- 저장 ---
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(out_path, engine="xlsxwriter") as w:
        df_out.to_excel(w, index=False, sheet_name="Output")
        if not df_issues.empty:
            df_issues.to_excel(w, index=False, sheet_name="Issues")

        wb = w.book
        bold = wb.add_format({"bold": True})
        for sheet in w.sheets:
            w.sheets[sheet].set_row(0, None, bold)

    print(f"✅ Gibson 계산 완료: {out_path}")

    # (선택) 자동으로 결과 파일 열기
    try:
        os.startfile(out_path)  # Windows
        print("📂 결과 파일을 열었습니다.")
    except Exception:
        pass

    return df_out

# --- 사용자 입력 ---
input_file = _strip_quotes(input("입력 파일 경로 (.xlsx 또는 .csv): ").strip())
output_file = _strip_quotes(input("결과 저장 파일 이름 (.xlsx): ").strip())

vector_length_bp = int(input("Vector 길이 (bp): ").strip())
vector_conc_ng_ul = float(input("Vector 농도 (ng/µL): ").strip() or 100)
dna_mix_total_ul = float(input("총 DNA mix 부피 (µL): ").strip() or 5)
insert_to_vector_molar = float(input("Insert:Vector 몰비 (예: 3): ").strip() or 3)
round_unit_ul = float(input("피펫 반올림 단위 (예: 0.1 µL): ").strip() or 0.1)

# --- 실행 ---
df_result = run_ratio_mode_fixed(
    input_path=input_file,
    output_path=output_file,
    vector_length_bp=vector_length_bp,
    vector_conc_ng_ul=vector_conc_ng_ul,
    dna_mix_total_ul=dna_mix_total_ul,
    insert_to_vector_molar=insert_to_vector_molar,
    round_unit_ul=round_unit_ul,
)

print(df_result.head(10).to_string(index=False))
