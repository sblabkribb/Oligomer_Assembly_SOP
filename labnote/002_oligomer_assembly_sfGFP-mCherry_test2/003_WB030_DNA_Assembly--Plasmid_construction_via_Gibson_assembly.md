---
title: WB030 DNA Assembly - Plasmid construction via Gibson assembly
experimenter: 윤예린
created_date: '2025-11-25'
end_date: ''
last_updated_date: '2025-12-01'
---

## [WB030 DNA Assembly] Plasmid construction via Gibson assembly
> 본 워크플로는 정제된 sfGFP-mCherry assembly PCR 산물을 벡터 백본과 결합하여 최종 플라스미드 형태로 조립하는 Gibson assembly 과정을 다룬다. 이 단계에서는 Gibson Assembly 를 수행하기 위해 필요한 Insert 및 Vector DNA 의 농도 및 부피를 python script 를 통해 계산하고, 이를 바탕으로 Gibson assembly 반응 혼합물을 manual로 준비하고 반응을 진행하였다.  


## 🗂️ Related Unit Operations

- [USW340 Computation - Gibson assembly mix calculation](#usw340-computation-gibson-assembly-mix-calculation)
- [UHW010 Liquid Handling - Gibson assembly reaction mixture preparation](#uhw010-liquid-handling-gibson-assembly-reaction-mixture-preparation)
- [UHW180 Incubation - Gibson assembly reaction](#uhw180-incubation-gibson-assembly-reaction)   




### [USW340 Computation] Gibson assembly mix calculation

- **Description**: 본 단계에서는 Gibson Assembly 반응을 위해 필요한 Insert와 Vector의 농도 및 부피를 계산하였다. 이를 위해 Python 스크립트를 활용하여 각 시료의 DNA 농도와 요구되는 molar ratio를 기반으로 최적의 혼합 비율을 산출하였다. 계산된 결과는 이후 Gibson Assembly 반응 준비에 활용되었다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-25'
- End_date: '2025-11-25'

#### Input
- DNA concentration data (from NanoDrop measurements)
    [251125_input.xlsx](./resources/gibson_assembly/251125_insert_concentration.xlsx)
- gibson_mix_calculation script 
    [gibson_mix_calculator_v1.py](./resources/gibson_assembly/gibson_mix_calculator_v1.py)
    [gibson_mix_calculator_v1.ipynb](./resources/gibson_assembly/gibson_mix_calculator_v1.ipynb)

#### Reagent
- (None)

#### Consumables
- (None)

#### Equipment
- Cpmputer

#### Method
1. Python 스크립트 [gibson_mix_calculation_v1.py](./resources/gibson_assembly/gibson_mix_calculation_v1.py) 또는 Jupyter Notebook [gibson_mix_calculation_v1.ipynb](./resources/gibson_assembly/gibson_mix_calculation_v1.ipynb)을 실행한다.
2. 안내에 따라 아래 파라미터를 순서대로 입력한다.
   - **입력 파일 경로**:  
     - Windows 파일 탐색기에서 input 파일을 선택한 뒤 `Ctrl + Shift + C`로 **전체 경로를 복사**하여 입력 창에 붙여넣기 한다.
   - **출력 파일 이름**: `251125_results.xlsx` 입력한다. (확장자명 까지 포함해야함.)
   - **Vector 길이 (bp)**: `1857`
   - **Vector 농도 (ng/µL)**: `100`
   - **Total DNA volume (µL)**: `5`
   - **Insert : Vector molar ratio**: `3`
   - **피펫 반올림 단위 (µL)**: `0.1`

* Vector 농도는 100 ng/µL 희석하여 사용하였다. 
* Gibson assembly reaction mixture 를 total 10 µL 로 준비하기 위해, DNA volume 을 5 µL 로 설정하였다.
* Insert : Vector molar ratio 는 3:1 로 설정하였다.


#### Output
- [251125_results.xlsx](./resources/gibson_assembly/251125_gibsonmix.xlsx)

#### Results & Discussions
- Gibson Assembly 반응 준비를 위해 Insert와 Vector의 농도 및 필요 부피를 자동 계산하였다.
- 계산 결과는 [`251125_gibsonmix.xlsx`](./resources/gibson_assembly/251125_gibsonmix.xlsx)에 저장되었으며, 이후 Gibson Assembly 반응 혼합물 준비 시 활용될 예정이다.
  

---

### [UHW010 Liquid Handling] Gibson assembly reaction mixture preparation

- **Description**: 본 단계에서는 Gibson Assembly 반응을 위해 계산된 Insert와 Vector의 농도 및 부피를 바탕으로 반응 혼합물을 수동으로 분주하였다.

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-26'
- End_date: '2025-11-26'

#### Input
- **Linearized vector DNA**  
  - pRSF backbone  
  - Working concentration: 100 ng/µL (diluted)

- **Insert DNA samples**  
  - Purified sfGFP-mCherry assembly PCR products 


- **Gibson Assembly reaction mix calculation results**  
  - 분주해야 할 Insert 및 Vector 부피가 포함된 계산 파일  
  - [251125_results.xlsx](./resources/gibson_assembly/251125_gibsonmix.xlsx)

#### Reagent
- Gibson Assembly Master Mix (NEB, M5510AA, Lot #10265621)

#### Consumables
- 96-well PCR plate (Biorad)
- Tips
- Sealing film

#### Equipment
- Pipettes
- Automated Roll Heat Sealer (formerly a4S) (AZENTA)
- Microplate Centrifuge (MP-2500) (MIIXLAB) 

#### Method
1. [251125_results.xlsx](./resources/gibson_assembly/251125_gibsonmix.xlsx) 파일을 열어 각 시료별로 필요한 Insert 및 Vector DNA의 분주 부피를 확인한다.

2. 96-well PCR plate에 각 시료별 Gibson Assembly 반응 혼합물을 다음과 같이 준비한다:
   - **Gibson Assembly Master Mix**: 5 µL  
   - **Insert DNA**: 계산된 부피  
   - **Vector DNA**: 계산된 부피  
   - **Total reaction volume**: 10 µL

3. 모든 시료에 대해 분주가 완료되면, plate를 마이크로플레이트 원심분리기에 넣고 가볍게 스핀다운하여 반응액을 well 바닥으로 모은다.

4. 원심분리 후, plate sealer에 넣고 sealing film을 부착하여 밀봉한다. 


#### Output
- Gibson Assembly reaction mixtures (96-well PCR plate, 12 samples)

#### Results & Discussions
- Gibson Assembly 반응 혼합물을 준비하였다.
- 이후 단계에서 Gibson Assembly 반응을 진행할 예정이다.


---

### [UHW180 Incubation] Gibson assembly reaction

- **Description**: 본 단계에서는 준비된 Gibson Assembly 반응 혼합물을 이용해 Gibson Assembly 반응을 수행하였다. 

#### Meta
- Experimenter: 윤예린
- Start_date: '2025-11-26'
- End_date: '2025-11-26'
- duration: 35 min

#### Input
- Gibson Assembly reaction mixtures (96-well PCR plate, 12 samples)

#### Reagent
- (None)

#### Consumables
- (None)

#### Equipment
- T-Roboot II (Biometra) - 3번

#### Method
#### Method
1. Gibson Assembly 반응 혼합물이 담긴 96-well PCR plate를 Biometra TRobot II 장비에 장착한다.

2. 장비에서 아래 설정으로 프로그램을 불러와 반응 조건을 설정한다:
   - **Program**: `GIBSON1`
   - **Temperature**: 50 °C  
   - **Incubation time**: 30 min  


3. `start` 버튼을 눌러 프로그램을 시작하여 반응을 진행한다. 반응이 완료될 때까지 기다린다.

4. 반응 종료 후, `stop` 버튼을 눌러 프로그램을 정지시키고 `open` 버튼을 눌러 lid를 열고 plate를 꺼낸 뒤 다음 단계로 진행한다.

#### Output
- Gibson Assembled DNA samples (96-well PCR plate, 12 samples)

#### Results & Discussions
- Gibson Assembly 반응을 수행하였다.
- 후속 단계에서 조립된 DNA 샘플을 이용해 형질전환을 진행할 예정이다.


