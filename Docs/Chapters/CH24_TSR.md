# CH24 TSR과 시간적 재구성

## 무엇인가

TSR은 Temporal Super Resolution으로, 현재 프레임과 히스토리를 활용해 목표 출력 해상도의 이미지를 재구성하는 UE의 시간적 업스케일러입니다.

## 렌더링에서 맡는 역할

낮은 내부 해상도로 장면을 계산하면서 높은 출력 해상도를 제공할 수 있게 합니다. 경계를 안정시키는 시간적 누적을 해상도 재구성과 연결하는 시스템입니다.

## 입력과 출력

입력은 내부 해상도의 장면 색, 이동·깊이 정보와 히스토리 등입니다. 출력은 목표 해상도의 이미지입니다. 입력 픽셀 수와 표시할 픽셀 수는 같지 않을 수 있습니다.

## 작동 과정

Screen Percentage 등으로 내부 렌더링 해상도를 정합니다. 가로·세로 비율을 함께 낮추면 장면을 계산할 픽셀 수가 더 크게 줄어듭니다.

이동 정보를 이용해 과거 세부를 현재 위치에 대응시키고 현재 샘플과 결합합니다. 단순히 한 장을 늘리는 것보다 시간적으로 얻은 정보를 활용합니다.

신뢰할 수 없는 히스토리를 처리하며 목표 출력으로 재구성합니다. 새로 드러나는 글자·얇은 선·빠른 반사는 입력 정보의 부족을 드러내기 쉽습니다.

![Epic 공식 TSR 비교 · 왼쪽 네이티브 4K, 오른쪽 1080p에서 4K로 재구성한 결과의 같은 구역을 발췌했습니다.](../Images/External/tsr-output-print.png)

Epic 공식 TSR 비교 · 왼쪽 네이티브 4K, 오른쪽 1080p에서 4K로 재구성한 결과의 같은 구역을 발췌했습니다.

읽을 곳  출력 크기가 같아도 들어온 정보량은 다릅니다. 글자·창틀 같은 세부를 비교하되 정지된 한 장이 이동 품질을 보장하지는 않습니다. UE 5.5 원문 장면의 성능 수치를 이 프로젝트의 예상 이득으로 사용하지 않습니다.

[© Epic Games · 공식 문서 · 출처 58](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine?application_version=5.5)

원본 일부 발췌·확대 · 색상 유지 · 표제 추가

원저작권과 원문 출처 표시는 유지합니다

## 왜 배경 제작에 필요한가

목표 기기의 화면 품질과 GPU 예산을 맞출 때 필요합니다. 출력 해상도만 보고 같은 화질이라고 결정하지 말고 내부 해상도와 이동 결과를 함께 봅니다.

## 성능과 제작 비용

장면의 화면 단위 작업을 줄일 수 있지만 TSR 자체의 처리·저장 비용과 고정 비용은 남습니다. 입력 픽셀 감소율이 총 프레임 시간 감소율은 아닙니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

출력 크기를 유지하고 입력 해상도에 따른 총 시간과 이동 품질을 비교합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part04_LightingAndImageQuality/CH24_TSR/Maps/L_CH24_TSR`

### 실습 절차

출력 크기와 Dynamic Resolution을 고정합니다. TSR을 유지한 채 Screen Percentage 100과 67을 비교합니다. 같은 경로의 글자·철망·반사를 녹화하고 전체 GPU 시간과 TSR 시간을 따로 기록합니다.

### 예상 결과와 이유

67%는 가로·세로 각각의 비율이므로 입력 픽셀 수는 약 45%가 됩니다. 화면 단위 작업은 줄 수 있지만 재구성 비용과 고정 비용 때문에 전체 시간이 같은 비율로 줄지는 않을 것입니다.

### 결과를 어떻게 해석할까

정지 상태의 선명도와 이동·가림 해제의 품질을 나눠 판정합니다. TSR 패스가 늘거나 유지돼도 다른 패스의 절감으로 전체가 빨라질 수 있습니다.

## 이 챕터에서 기억할 것

TSR은 시간적 정보를 이용한 출력 이미지 재구성입니다. 내부 해상도의 절감과 실제 이동 화질·전체 시간을 함께 판단합니다.

## 이해한 뒤 확인할 조건

외부 비교의 장비·장면 성능을 자신의 예상 이득으로 사용하지 않습니다. TAAU와 다른 업스케일러는 별도 비교 대상입니다.

## 공식 자료와 확장

- [Anti-Aliasing and Upscaling](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine)
- [Temporal Super Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
