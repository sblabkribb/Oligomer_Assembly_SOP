---
title: WB040 DNA Purification - Oligomer Assembly DNA Purification
experimenter: 윤예린
created_date: '2025-11-04'
end_date: '2025-11-04'
last_updated_date: '2025-11-12'
---

## [WB040 DNA Purification] Oligomer Assembly DNA Purification
> 본 워크플로는 Oligomer Assembly 과정에서 생성된 DNA 산물을 정제하여, 후속 (Gibson assembly) 반응에 적합한 품질의 DNA를 확보하는 것을 목표로 한다.
> 정제 방식은 매뉴얼 방식과 자동화 시스템(Zypher)을 이용한 두 가지 방법을 포함하며, 각 방법에서 얻어진 정제 DNA는 NanoDrop을 이용해 농도를 측정하고 비교하였다. 

## 🗂️ Related Unit Operations
- [UHW250 Nucleic Acid Purification - Manual PCR product purification](#uhw250-nucleic-acid-purification-manual-pcr-product-purification)
- [UHW250 Nucleic Acid Purification - Automated Magnetic Bead-based Purification (Zypher System)](#uhw250-nucleic-acid-purification-automated-magnetic-bead-based-purification-zypher-system)
- [UHW400 Manual - DNA Concentration Measurement using NanoDrop Spectrophotometer](#uhw400-manual-dna-concentration-measurement-using-nanodrop-spectrophotometer)


---

### [UHW250 Nucleic Acid Purification] Manual PCR product purification

- **Description**: 본 단계에서는 Recovery PCR product를 대상으로 마그네틱 비드 기반 정제 키트를 이용해 DNA를 정제하였다. 이 과정은 단백질, 염, 프라이머 등의 반응 부산물을 제거하고 순수한 DNA를 회수하기 위한 단계로, 이후 Gibson Assembly 반응에 사용할 수 있도록 시료 품질을 확보하는 것을 목표로 한다. 정제는 **매뉴얼 방식(manual handling)** 으로 수행하였으며, 정제 효율과 DNA 농도는 후속 실험을 통해 확인하였다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-4'
- End_date: '2025-11-4'  
- duration: 1 hr (12 samples)

#### Input
- Recovery PCR product (1.5 mL E-tube, 12 samples)

#### Reagent
- MagListo™ 5M PCR/Gel Purification Kit (Bioneer, Lot #23031J)
- Ethanol (absolute grade, 제조사, Lot # 확인 필요)
- 2-Propanol (Supelco, Lot #I1160534 128)

#### Consumables
- 1.5 mL E-tube
- Tips

#### Equipment
- Vortex-Genie 2 mixer (Scientific Industries)
- Pipettes (p100, p1000)
- Magnetic rack
- Centrifuge (Eppendorf)
- ThermoMixer C (Eppendorf)

#### Method
- **실험 프로토콜**은 [MagListo™ 5M PCR/Gel Purification Kit (Bioneer) 매뉴얼](./resources/manuals/UG_MagListo_PCR_Gel_Purification_Kit.pdf) 에 따라 수행하였다.
주요 단계는 다음과 같다. 
1. PCR product를 1.5 mL E-tube에 옮기고, Binding buffer를 5배 부피만큼 첨가하고 잘 혼합한다.
2. 혼합물을 Magnetic Bead solution 100 μL과 함께 첨가후 완전히 혼합한다. (pipetting 또는 vortexing)
3. Magnetic rack에 튜브를 놓고 비드가 자석에 결합될때까지 기다린 후, 상등액을 pipette으로 제거한다. 
4. W2 Buffer 700 μL을 첨가하여 비드를 세척한다. 다시 자석에 놓고 상등액을 제거한다.
5. Absolute ethanol 700 μL을 첨가하여 비드를 추가로 세척한다. 다시 자석에 놓고 상등액을 제거한다.
6. 60°C로 예열한 heat block 위에 약 5분간 건조하여 에탄올을 완전히 증발시킨다.
7. Elution buffer 40 μL을 첨가하고, 비드와 완전히 혼합한 후, 60 °C에서 1 분간 반응시킨다.
8. Magnetic rack에 놓고 상등액(DNA 용출액)을 새로운 E-tube에 옮긴다.


#### Output
- Purified DNA samples
  - Tube type: 1.5 mL E-tube
  - Total: 12 samples
  - Sample IDs: A1, B1, C1, D1, E1, F1, G1, H1, A2, B2, C2, D2
  
#### Results & Discussions
- 정제된 DNA의 농도는 후속 실험에서 측정할 예정이다. 


---

### [UHW250 Nucleic Acid Purification] Automated Magnetic Bead-based Purification (Zypher System)

- **Description**: 본 단계에서는 **Zypher** 자동화 시스템을 이용하여 Recovery PCR product의 DNA 정제(purification)를 수행하였다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-04'
- End_date: '2025-11-04'
- duration: 1 hr

#### Input
- Recovery PCR product (96-well PCR plate, 36 samples)

#### Reagent
- MagListo™ 5M PCR/Gel Purification Kit (Bioneer, Lot #23031J)
- Ethanol (absolute grade, 제조사, Lot # 확인 필요)

#### Consumables
- Zypher tip box * 2
- 96-well PCR plate (BioRad) * 2
- 96 well storplate * 3
- 96 deep well plate (PerkinElmer) * 1

#### Equipment
- Zypher  
  

#### Method
1. Zypher 기기의 3가지 전원을 모두 켠 후, 컴퓨터 바탕화면의 Zypher 제어 소프트웨어(Maestro) 아이콘을 클릭하여 실행한다.
   - 기기와 소프트웨어 연결에는 다소 시간을 소요될 수 있다.
2. 연결이 완료되는 동안, 아래 사진에 따라 필요한 plates 및 tips을 준비한다. purification에 필요한 plate layout은 아래와 같다. 이는 바탕화면에서도 확인할 수 있다. 
     <img src="./resources/images/PCRpurification.png" alt="PCR purification setup" >
3. Maestro 소프트웨어에서 다음 경로로 프로토콜을 불러온다.
`[Open Maestro Application] → [Purification] → Purification1_30-50ul`
   * 본 프로토콜은 30–50 μL PCR product 정제에 적합하다.
4. 각 plate의 label 및 위치가 Zypher deck layout과 일치하도록 배치한다.
   - C3 위치: magnetic plate를 먼저 장착한 후, 그 위에 PB buffer plate를 올린다.
   - Waste plate: 세척 후 재사용 가능하므로, 깨끗이 세척·건조된 plate를 사용한다.
5. 알맞게 장착되었는지 Deck 방향과 기기 정면 및 옆면에서 모두 확인한다.
6. A3 위치의 Elution buffer plate는 `Lid`로 표시된 plate이며, 여기에 **Universal Lid**를 덮는다. 
7. Maestro 소프트웨어에서 [Run] 버튼을 클릭하여 purification 프로세스를 시작한다. 
8. 프로세스 중 `Lubrication step`(윤활 단계)이 자동으로 포함되어 있다.
    - User Message에
    > `Place Lubricator at C3!!` 라는 알림이 표시되면, Zypher 기기 C3 위치에 Lubricator 를 뚜껑을 열고 올려놓는다.

     - 이때 원래 C3 위치에 있던 PB buffer plate와 magnetic plate는 일시적으로 제거하여 옆에 둔다.
     - Lubrication: 정전기, 마찰열, 마모를 방지하기 위해 윤활유를 도포하는 과정.
9. Lubrication step이 완료되면 lubricator를 제거하고, 미리 꺼내둔 PB buffer plate와 magnetic plate를 다시 C3 위치에 장착한다.
     - 이후 `OK` 버튼을 클릭하여 프로세스를 계속 진행한다.
10. `Please enter the number of columns to process` 창이 뜨면, 정제할 sample 수에 맞게 column 수를 입력한다.
11.  이후 tip을 가져가면서 프로세스가 프로토콜에 따라 purification이 진행된다.
12.  프로그램이 완료되면 모든 plate를 꺼내고, 사용한 tip rack은 폐기, waste plate는 세척 후 보관한다.
13. 정제된 DNA가 담긴 Elution plate는 바로 다음 단계에 사용하거나, sealing film으로 밀봉 후 보관한다.


#### Output
- Purified Recovery PCR product (96-well PCR plate, 36 samples)

#### Results & Discussions
- Purified Recovery PCR product를 확보하였다. 
- 후속 단계에서 DNA 농도를 측정할 예정이다.
- 모든 well에서 소량의 magnetic bead가 남아있는 것을 확인하였다. 후속 실험에서 영향이 있는지 확인 할 예정이다. 

  

---

### [UHW400 Manual] DNA Concentration Measurement using NanoDrop Spectrophotometer

- **Description**:  본 단계에서는 정제된 Recovery PCR product의 DNA 농도(concentration)를 측정하기 위해 NanoDrop spectrophotometer를 사용하였다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-04'
- End_date: '2025-11-04'

#### Input
- Purified DNA samples (1.5 mL E-tube, 12 samples)
- Purified DNA samples (96-well PCR plate, 36 samples)

#### Reagent
- Elution Buffer — MagListo™ 5M PCR/Gel Purification Kit (Bioneer, Lot #23031J)

#### Consumables
- Tips
- Kimwipes

#### Equipment
- NanoDrop 2000c Spectrophotometer (Thermo Fisher Scientific)
- Pipettes (p2.5)

#### Method
1. NanoDrop 전원을 켜고, DNA measurement mode를 선택한다.  
2. Blank 측정을 위해 Elution Buffer 1.5μL를 측정 플랫폼에 떨어뜨리고 [Blank] 버튼을 클릭한다.  
3. 각 시료를 1.5μL씩 측정하여 농도(ng/μL)값을 기록한다.  
4. 각 시료 측정 후 Kimwipe로 렌즈 표면을 닦아 교차오염을 방지한다. 
5. 모든 시료 측정이 완료되면, 데이터를 저장하고 NanoDrop 전원을 끈다.
 

#### Output
- Purified DNA samples (48 samples)
- DNA concentration data 
  - [Plate_Layout_Concentration.xlsx](./resources/Plate_Layout_Concentration.xlsx)

#### Results & Discussions
- 정제된 Recovery PCR product의 DNA 농도를 측정하였다. 
- 수동으로 정제한 DNA 샘플 12개와 Zypher 시스템으로 정제한 DNA 샘플 36개의 농도 데이터를 확보하였다.
- 수동의 정제한 DNA 샘플의 평균 농도는 59.2 ng/μL였으며, Zypher 시스템으로 정제한 DNA 샘플의 평균 농도는 22.9 ng/μL로 나타났다. 
- Zypher 시스템을 이용한 정제 샘플의 농도가 상대적으로 낮게 측정되어, 정제 이전 단계인 Recovery PCR 반응 cycle 수를 늘려보는 방안을 고려하고자 한다.








