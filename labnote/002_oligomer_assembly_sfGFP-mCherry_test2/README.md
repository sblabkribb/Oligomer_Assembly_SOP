---
title: oligomer assembly_sfGFP-mCherry_test2
author: '윤예린'
experiment_type: labnote
created_date: '2025-11-25'
last_updated_date: '2025-12-01'
---

## 🎯 Experiment Objective

> 본 실험의 목적은 약 1.7 kb 크기의 sfGFP–mCherry DNA cassette를 oligomer pool assembly 방식으로 합성하고, oligo 기반 유전자 합성 프로세스의 효율성과 정확도를 정량적으로 평가하며, 전체 워크플로우를 SOP 수준으로 재현·표준화하는 것이다.
**본 실험은 이전에 수행한 동일 target 서열 기반의 sfGFP–mCherry assembly 실험의 반복 실험으로, 실험 재현성(reproducibility) 및 공정 신뢰성(process reliability) 을 검증하는 데 중점을 둔다.**

#### 1. 배경 및 문제점

이전 실험에서는 다음과 같은 문제가 발생했다. 

- transformation 단계에서 단일 콜로니 확보가 어려움
- colony 색 기반 phenotype 판별의 불확실성 증가
- colony picking 기준이 불명확하여 시퀀싱 결과의 해석 신뢰도 저하

그래서 이전 실험에서 테스트한 여러가지 변수들의 영향을 명확히 분리하여 평가하기 어려웠다. 따라서 이번 실험에서는 우선적으로 몇 가지 변수들만을 선택하고, 단일 콜로니를 확보 할 수 있도록 transformation 공정을 최적화 하여 각각의 영향력을 독립적으로 분석할 수 있도록 실험 설계를 개선하고자 한다.

#### 2. 이번 실험에서의 개선 전략

이러한 문제를 보완하기 위해, 이번 실험에서는 핵심 변수만을 분리하여 조절하고 아래 조건을 표준화하였다.

- Oligo pool 농도 조건: 25 fmol/µL, 2.5 fmol/µL 두 조건만 테스트
- Hybridization 단계: 생략하여 assembly PCR의 순수한 농도 효과만 평가
- Error Correction: T7 Endonuclease I(0.5 U/µL) 처리 유지
→ error correction 효과만을 독립적으로 분석할 수 있도록 설계

#### 3. Downstream 공정 최적화

본 실험에서는 transformation 및 plating 조건 또한 개선하여 단일 colony 확보율을 최적화한다.

- spotting 조건을 최적화하여 green / red / dual fluorescence / white
등 phenotype-based classification을 명확하게 수행
- phenotype 기반 1차 스크리닝을 통해 oligomer assembly 성공률을 초기 단계에서 평가

#### 4. 최종 정확도 및 상관관계 분석

선택된 colony에 대해 Sanger sequencing을 수행하여 다음을 평가한다.
- assembly accuracy (염기서열 정확도)
- phenotype–genotype correlation
(형광 발현 패턴과 실제 염기서열의 일치 여부)

## 🗂️ Related Workflows

[ ] [001 WB010 DNA Oligomer Assembly - sfGFP-mCherry oligomer assembly test2](./001_WB010_DNA_Oligomer_Assembly--sfGFP-mCherry_oligomer_assembly_test2.md)

[ ] [002 WB040 DNA Purification - sfGFP-mCherry assembly product purification](./002_WB040_DNA_Purification--sfGFP-mCherry_assembly_product_purification.md)

[ ] [003 WB030 DNA Assembly - Plasmid construction via Gibson assembly](./003_WB030_DNA_Assembly--Plasmid_construction_via_Gibson_assembly.md)


[ ] [004-1 WB120 Biology-mediated DNA Transfers - Transformation of Gibson assembly products into *E. coli*](./004_WB120_Biology-mediated_DNA_Transfers--Transformation%20of%20Gibson%20assembly%20products%20into%20E.%20coli.md)

[ ] [004-2 WB120 Biology-mediated DNA Transfers - Transformation of Gibson assembly products into *E. coli*](./005_WB120_Biology-mediated_DNA_Transfers--Transformation_of_Gibson_assembly_products_into_E._coli.md)

