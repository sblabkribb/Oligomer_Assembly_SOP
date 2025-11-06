---
title: WD050 DNA Oligomer Pool Design - sfGFP-mCherry oligomer pool design
experimenter: 윤예린
created_date: '2025-10-13'
end_date: '2025-10-15'
last_updated_date: '2025-11-4'
---

## WD050 DNA Oligomer Pool Design - sfGFP-mCherry oligomer pool design

> 본 워크플로는 sfGFP–mCherry 융합 유전자를 대상으로, oligo pool 기반 DNA assembly 실험을 수행하기 위한 유전자 카세트 설계 및 oligo pool 디자인 과정을 다룬다.


## 🗂️ Related Unit Operations
- [USW005 Biological Database — Design of Expression Cassette for Oligomer Assembly](#usw005-biological-database--design-of-expression-cassette-for-oligomer-assembly)
- [USW030 Vector Design - for sfGFP–mCherry Oligomer Assembly](#usw030-vector-design---for-sfgfpmcherry-oligomer-assembly)
- [USW020 Primer Design - Vector & Assembly primer design](#usw020-primer-design---vector--assembly-primer-design)
- [USW010 DNA Oligomer Pool Design - sfGFP–mCherry oligo pool design & order](#usw010-dna-oligomer-pool-design---sfgfp-mcherry-oligo-pool-design--order)




---------------------------------------------------------

### [USW005] Biological Database — Design of Expression Cassette for Oligomer Assembly

**Description**  : 본 실험은 sfGFP–mCherry 융합 유전자의 발현을 위한 유전자 카세트(expression cassette) 를 설계하는 것을 목표로 한다. 발현 가능한 형태의 카세트를 구축하기 위해 promoter, RBS, terminator 를 포함한 전체 구조를 설계하였다. 이를 위해 iGEM Registry of Standard Biological Parts (https://parts.igem.org/
) 를 활용하여, constitutive promoter, bacterial RBS, terminator 부품을 각각 검색·비교하고 최종적으로 선정하였다.

#### Meta
- **Experimenter**: 윤예린  
- **Start_date**: '2025-10-13'  
- **End_date**: '2025-10-13'

#### Input

| Category       | Name (Part ID)    | Sequence / File                                                                                                                   | Description                                                       | Source / Link                                                                                                                               |
| -------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Promoter**   | **BBa_J23110**    | `tttacggctagctcagtcctaggtacaatgctagc`                                                                                             | *Medium–low strength constitutive promoter* (Anderson Collection) | [iGEM Registry – Anderson Promoters](https://parts.igem.org/Promoters/Catalog/Anderson)                                                     |
| **RBS**        | **BBa_B0030**     | `TCTAGAGATTAAAGAGGAGAAATACTAG`                                                                                                    | *Medium–low strength prokaryotic ribosome binding site*           | [iGEM Registry – Prokaryotic Constitutive RBS](https://parts.igem.org/Ribosome_Binding_Sites/Prokaryotic/Constitutive/Community_Collection) |
| **CDS**        | **sfGFP–mCherry** | [sfGFP_GGSGGS_mCherry.dna](./resources/vector_map/sfGFP_GGSGGS_mCherry.dna)                                                     | sfGFP–linker(GGSGGS)–mCherry fusion gene                          | Provided by 김홍연 연구원                                                                                                                         |
| **Terminator** | **BBa_B0015**     | `aggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctctactagagtcacactggctcaccttcgggtgggcctttctgcgtttata` | rrnB T1 + T7 double terminator                                    | [iGEM Registry – BBa_B0015](https://parts.igem.org/Part:BBa_B0015)                                                                          |



#### Reagents
- (None)

#### Consumables
- (None)

#### Equipment

-   Computer
-   Software: SnapGene
-   Database: iGEM Registry 

#### Method 

1. iGEM Registry of Standard Biological Parts (https://parts.igem.org/) 에 접속한다.
2. 상단 검색창 또는 카테고리에서 적합한 부품들 (promoter, RBS, terminator)을 각각 검색한다.
3. 각 부품의 특성(발현 강도, 호환성, 적용 가능한 host system 등) 을 검토하여 실험 목적에 가장 부합하는 조합을 선정한다.  
4. SnapGene 을 이용하여 각 부품들을 서열을 순차적으로 연결하고, 전체 유전자 카세트를 시각화 한다. 
5. 필요한 경우 주요 feature (promoter, RBS, CDS, terminator 등) 들을 추가하고, ORF가 올바르게 연결되었는지 검토한다.
6. 최종 서열 파일을 저장한다. 


#### Output
- 저장된 유전자 카세트 서열 파일 : [`sfGFP_mCherry_cassette.dna`](./resources/vector_map/sfGFP_mCherry_cassette.dna)
- Construct overview : ` Promoter (BBa_J23110) – RBS (BBa_B0030) – sfGFP_mCherry – Terminator (rrnB T1) `


#### Results & Discussions
- 본 실험에서는 아래 부품들을 최종 선정하였다.  
   - **Promoter** : BBa_J23110 (medium–low strength, constitutive promoter)  
   - **RBS** : BBa_B0030 (medium–low strength)  
   - **Terminator** : BBa_B0015 (rrnB T1 + T7 terminator)
- Promoter / RBS 선정 이유  : 형광 발현도 확인하고, 세포 성장에 부담을 줄이기 위해 중간 이하 세기의 constitutive promoter (BBa_J23110) 와 RBS (BBa_B0030) 를 선택하였다.
- Terminator 선정 이유 : rrnB T1 terminator 는 안정적인 전사 종결을 위해 널리 사용되는 부품으로, 본 실험에서도 적합하다고 판단되어 선택하였다.
- 향후 계획 : 본 단계에서 설계된 유전자 카세트 서열을 기반으로 gibson assembly 를 위한 overlap 서열을 최종적으로 추가하여 oligo assembly용 insert 서열을 디자인할 예정임.  
    - ` overlap 1 (30bp) - Promoter (BBa_J23110) – RBS (BBa_B0030) – sfGFP_mCherry – Terminator (rrnB T1) - overlap 2 (30bp) `
 
---------------------------------------------------------

### USW030 Vector Design - for sfGFP–mCherry Oligomer Assembly

**Description** : 본 단계에서는 oligomer assembly의 정확성을 검증하기 위한 sfGFP–mCherry vector 를 설계하였다.
assembly가 올바르게 이루어졌는지를 확인하기 위해, 조립된 sfGFP–mCherry DNA fragment 를 pRSFDuet vector backbone 에 cloning 한 후 E. coli DH5α 에 transformation하여 형광 발현 여부를 검증하는 downstream 실험을 계획하였다.
이를 위해 본 단계에서는 실험 설계에 필요한 vector backbone을 선정하고, sfGFP–mCherry cassette 삽입을 위한 overlap sequence를 디자인하여 최종 vector 구조를 확정하였다. 또한, oligomer assembly 수행에 사용할 insert 서열 역시 함께 설계하였다.
  

#### Meta

-   Experimenter: 윤예린
-   Start_date: '2025-10-13'
-   End_date: '2025-10-13'

#### Input

| Part | Name | Sequence / File | Description | Source |
|---------------|---------------|---------------|---------------|---------------|
| Vector | pRSF-Duet | [vector_pRSFduet.dna](./resources/vector_map/vector_pRSFduet.dna) | RSF origin, KanR | 김홍연 연구원 |
| Insert | sfGFP-mCherry cassette | [sfGFP_mCherry_cassette.dna](./resources/vector_map/sfGFP_mCherry_cassette.dna) | sfGFP-mCherry expression cassette | this study |


#### Reagents
(None)


#### Consumables
(None)

#### Equipment
- Computer
- Software : Snapgene

#### Method
1. pRSFDuet vector backbone 파일을 SnapGene에서 불러와 전체 서열을 확인한다.
2. Insert DNA fragment를 삽입하기 위한 적절한 위치를 선정하고, 필요에 따라 서열을 삭제 하거나 조정한다. 
3. 해당 위치에 앞서 디자인한 `sfGFP_mCherry_cassette.dna` 서열을 삽입한다. 
4. 서열 내 주요 feature (promoter, RBS, CDS, terminator 등)를 확인하고, ORF가 올바르게 연결되었는지 검토한다.
5. 삽입된 서열을 기반으로 Gibson assembly를 위해 필요한 overlap sequence를 디자인 한다.
   - overlap sequence의 길이는 30 bp로 설정하였음.
6. 필요에 따라 SnapGene 에서 overlap sequence를 feature로 추가하여 시각적으로 구분한다.
7. 최종적으로 디자인된 vector map과 oligomer assembly 를 수행하고자 하는 insert 서열을 각각 저장한다. 
    - 파일명: `final_pRSFduet_sfGFP_mCherry.dna` (최종 vector map) 
    - 파일명: `insert_sfGFP_mCherry_cassette.dna` (oligo assembly용 insert 서열)

   - 본 실험 설계에 따라, oligomer assembly를 수행하고자 하는 최종 타깃 서열을 다음과 같은 구성으로 디자인 하였음. 
    `overlap sequence 1 (30 bp)– Promoter (BBa_J23110) – RBS (BBa_B0030) – sfGFP_mCherry – Terminator (rrnB T1) - overlap sequence2 (30bp)`
#### Output

아래는 본 단계에서 생성된 vector map 파일

| File | Description |
|-------------------|----------------------------------|
| [insert_sfGFP_mCherry_cassette.dna](./resources/vector_map/insert_sfGFP_mCherry_cassette.dna) | oligomer assembly를 수행하고자 하는 최종 타깃 서열 (sfGFP–mCherry cassette, 약 1.7 kb) |
| [final_pRSFduet_sfGFP_mCherry.dna](./resources/vector_map/final_pRSFduet_sfGFP_mCherry.dna) | 최종 vector map |

#### Results & Discussions
- 설계된 overlap sequence는 다음과 같다.
  - **overlap sequence 1** (upstream) : `ctcatgttagtatccggatatagttcctcc`  
  - **overlap sequence 2** (downstream) : `cgcaattaatgtaagttagacccctatttg`


- 본 실험 설계에 따라, oligomer assembly를 수행하고자 하는 최종 타깃 서열을 다음과 같은 구성으로 디자인 하였음. 
    `overlap sequence 1 (30 bp)– Promoter (BBa_J23110) – RBS (BBa_B0030) – sfGFP_mCherry – Terminator (rrnB T1) - overlap sequence2 (30bp)`

- overlap sequence 크기는 30 bp로 설정하였으나, 실험 조건에 따라 조정하면서 최적화할 수 있음.
  
------------------------------------------------------------------------


### [USW020 Primer Design - Vector & Assembly primer design]

- **Description** : 본 단계는 cloning vector preparation 및 oligomer assembly 수행을 위한 primer 디자인 과정이다. 실험 목적에 따라 vector backbone 증폭용 primer와 oligomer assembly용 outer primer를 각각 설계하였다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-13'
- End_date: '2025-11-13'

#### Input
- Insert 서열 : [`insert_sfGFP_mCherry_cassette.dna`](./resources/vector_map/insert_sfGFP_mCherry_cassette.dna)
- Vector 서열 : [`vector_pRSFduet.dna`](./resources/vector_map/vector_pRSFduet.dna)

#### Reagent
- (None)

#### Consumables
- (None)

#### Equipment
- Computer
- Software : Snapgene

#### Method


**vector backbone PCR primer design**

  1. pRSFDuet vector backbone을 증폭을 위한 primer를 설계하기 위해 SnapGene 에서 `vector_pRSFduet.dna` 파일을 연다.
  2. overlap sequence 양 끝에서 부터 Tm 값이 57-59℃ 범위에 해당하도록 primer 를 디자인한다.
  3. 설계된 primer 서열은 다음과 같다.
        - pRSFduet_F1 : `cgcaattaatgtaagttagacccc`
        - pRSFduet_R1 : `ggaggaactatatccggatactaacat`

**oligomer assembly outer primer design**

   4. oligomer assembly 시 사용될 outer primer를 설계하기 위해 SnapGene 에서 `insert_sfGFP_mCherry_cassette.dna` 파일을 연다.
   5. overlap sequence 부분에서 Tm 값이 58-60°C 범위에 해당하도록 primer 를 디자인한다. 이 primers 는 assembly PCR 시 oligo pool 들과 함께 사용되므로, oligo pool 내 overlap 서열의 평균 Tm 값을 고려하여 동일한 온도 조건에서 효율적으로 결합이 이루어질 수 있도록 설계한다.
   
      - overlap_F1 : `ctcatgttagtatccggatatagttcctc`
      - overlap_R1 : `caaataggggtctaacttacattaattgcg`
  
**primer sequence 저장 및 주문**

6. 디자인 된 primer 서열을 마크로젠 주문 양식 파일에 정리하여 저장한다.
   - [primer_order_251015_sfGFP_mCherry.xls](./resources/primers_order/primer_order_251015_sfGFP_mCherry.xls)
7. 마크로젠 웹사이트 (https://dna.macrogen.com/main.do) 에서 Custom Oligo 서비스로 주문을 진행한다. 
    - 주문번호 : HO00426248
    - 주문일 : 2025-10-15
    - 서비스 : Custom Oligo

#### Output
- primer order file : [primer_order_251015_sfGFP_mCherry.xls](./resources/primers_order/primer_order_251015_sfGFP_mCherry.xls)
- primer summary table :

    | primer name | 5'-Seq-3'                      |Tm (°C)|
    |-------------|--------------------------------|-------|
    | overlap_F1  | ctcatgttagtatccggatatagttcctc  | 59.6  |
    | overlap_R1  | caaataggggtctaacttacattaattgcg | 58.9  |
    | pRSFduet_F1 | cgcaattaatgtaagttagacccc       | 57.4  |
    | pRSFduet_R1 | ggaggaactatatccggatactaacat    | 59.1  |

#### Results & Discussions
- oligo pool 디자인 시 각 oligo overlap 서열의 Tm 값을 대략 60 °C 로 설정할 계획이므로, outer primer의 Tm 값을 이에 맞추어 조정함으로써 assembly 반응의 효율을 향상시키고자 함. 


------------------------------------------------------------------------

### USW010 DNA Oligomer Pool Design - sfGFP-mCherry oligo pool design & order

-   **Description**: 본 단계에서는 sfGFP–mCherry cassette (\~1.7 kb)을 oligo 기반으로 합성하기 위해, Desembler를 사용하여 각 oligo의 길이, overlap, GC%, Tm 균형 등을 고려하여 디자인함. 

#### Meta

-   Experimenter: 윤예린
-   Start_date: '2025-10-13'
-   End_date: '2025-10-15'

#### Input

| NO. | File | Description |
|-----|-----------------------------|-------------------------------------------|
| 1   | [insert_sfGFP_mCherry_cassette.dna](./resources/vector_map/insert_sfGFP_mCherry_cassette.dna) | oligo assembly용으로 디자인된 1.7 kb insert 서열 |

#### Equipment
-   Computer
-   Software : Desembler, SnapGene

#### Method

**Desembler 를 이용한 oligo pools design**
1. Desembler (http://223.130.146.86:8088/)에 접속하여, 로그인한다. (ID: sblabuser, PW: Kribb1234!!)
2. Project 탭에서 화면 우측 상단의 `+ Add` 버튼을 클릭하여 새 프로젝트를 생성한다.
    - Project name: `assembly SOP`
3. Sample 탭에서 `+ Add` 버튼을 클릭하여 oligo pool design을 수행하고자 하는 DNA 서열을 추가한다.
    - Sample name: `sfGFP_mCherry`
    - Sequence input: `insert_sfGFP_mCherry_cassette.dna` 파일에서 서열 복사 후 붙여넣는다. 
    - Length: 1718
4. Design 탭에서
　① Select filters 에서 디자인하고자하는 서열이 추가된 프로젝트를 선택한다.   `oligomer assembly SOP` 
　② Select a DNA sample 에서 디자인하고자하는 서열을 선택한다. `sfGFP_mCherry`
　③ Design Parameters  에서 design 조건을 설정한다. 
    - 본 실험에서는 아래와 같은 조건으로 설정하였다.
      　- Maximum Oligomer Length: 100
      　- Maximum Overlap Length: 40
      　- Choose Tm for 5' overlap: 55
      　- Choose Tm for 3' overlap: 55
      　- Choose first strand : ✅ 5' exonuclease chewing back (first strand direction - 5' to 3')
5. Assembly 탭에서 생성된 결과를 클릭하여 새 창에서 디자인된 oligo pool 서열을 확인하고, 화면 하단의 `Generate Plot` 버튼을 클릭하여 oligo의 길이, 방향, 개수 등을 시각적으로 확인한다.
6. 추가적인 oligo 조정을 위해, 화면 우측 상단의 `edit sequence` 버튼을 클릭하여 optimizer 탭 (oligo 조정 페이지) 로 이동하여 조건 및 위치를 수동으로 조정한 후 저장한다.
7. 최종적으로 디자인된 oligo pool 서열 (`assembly ID : 429`) 을 Assembly 탭에서 찾아 선택하고, `Show details` 버튼을 클릭해서, 화면 상단 중앙의 `Download excel file` 버튼을 클릭하여 oligo pool 서열을 엑셀 파일로 다운로드 한다. 

**Manual oligo pool 확인 및 조정**
1. 다운로드한 oligo pool 엑셀 파일을 열어, Pool name 컬럼의 값을 순서대로 1부터 30 으로 변경한 후, 제목 행(header row)을 삭제하고 CSV 파일로 다른 이름으로 저장한다.
2. SnapGene에서 디셈블러로 디자인한 DNA 서열 (`insert_sfGFP_mCherry_cassette.dna`) 파일을 열고, 상단 메뉴에서 Primers → Import Primers → Import Primers from a List 를 클릭한다.
3. Import primers from a file: 항목에서 위에서 저장한 CSV 파일을 선택한 뒤, OK 버튼을 클릭하여 primer로 추가한다.
4. 추가된 primer를 확인한 후, 필요한 경우 각 oligo의 overlap 길이와 Tm 값을 수동으로 변경한다. 
   - 본 실험에서는 다음과 같은 기준으로 조정하였다.
   - overlap 길이를 20 nt 이상, Tm 값을 58 ~ 63 °C 범위로 조정함.
5. 조정이 완료 후 최종 oligo pool 파일을 엑셀 파일로 저장한다.
　- 파일명: [oligo_order_251015_sfGFP_mCherry.xlsx](./resources/oligopool_order/oligo_order_251015_sfGFP_mCherry.xlsx)



**Oligo pool 주문**

- **IDT**와 **TWIST** 두 업체에 견적 문의 및 구매 요청을 진행할 수 있다. 
   업체 별 주문 절차는 다음과 같다.

    **IDT**
   1.  주문 파일(`oligo_order_251015_sfGFP_mCherry.xlsx`)을 `hjy@genere.co.kr` (Geneer)에 전달하여 견적을 문의한다.
   2.  회신된 견적서를 확인 후, 나유진 박사님과 주문 계정 관련 사항을 협의한다. 
       - [견적서 파일 (Geneer IDT)](./resource/251015_IDT_oligopool_견적서.pdf)
   3.  구매 계정 확정 후, 구매요청서 작성하여 구매 진행한다.


  
    **TWIST**
   1. 주문 파일(`oligo_order_251015_sfGFP_mCherry.xlsx`)을 TWIST 공식 홈페이지에 직접 업로드하여 주문을 진행한다.
   2. 회신된 견적서를 확인 후, 나유진 박사님과 주문 계정 관련 사항을 협의한다.
      - [견적서 파일 (Xogene TWIST)](./resource/251015_TWIST_oligopool_견적서.pdf)
   3. 구매 계정 확정 후, 구매요청서 작성하여 구매 진행한다.

#### Output

| NO. | File | Description |
|-----------------|-----------------|--------------------|
| 1 | [oligo_order_251015_sfGFP_mCherry_58-61Tm.xlsx](./resources/oligopool_order/oligo_order_251015_sfGFP_mCherry_58-61Tm.xlsx) | overlap 길이 및 Tm 값이 포함된 oligo pool 파일 |
| 2 | [oligo_order_251015_sfGFP_mCherry.xlsx](./resources/oligopool_order/oligo_order_251015_sfGFP_mCherry.xlsx) | IDT, TWIST oligo pool 주문 파일 |

#### Results & Discussions

- Desembler를 사용하여 디자인된 oligo pool의 주요 특성은 다음과 같다.
    - 총 oligo 길이 합계 : 2,384 nt 
    - oligo 길이 : 70-92 nt (평균 79.5 nt)
    - overlap 길이 : 20-27 nt (평균 23 nt)
    - overlap Tm 값 : 58-62°C (평균 58.9°C)
    - 총 oligo 개수 : 30 개

    → 평균 oligo 길이가 약 80 nt 이므로 절반이 overlap 될 수 있도록 overlap 길이를 20 nt 이상으로 디자인했음.


- Desembler 사용 중, Optimizer 탭에서 마지막 oligo 서열이 수동으로 수정되지 않는 오류가 발생함. 
  → 확인 필요.

- TWIST 주문 건을 구매 취소하고, IDT에 주문 진행함. (2025-10-15)
- TWIST 구매 취소 하였으나, 주문서가 접수되어 oligo pool 이 제작되어 받았음. (2025-11-3) 


