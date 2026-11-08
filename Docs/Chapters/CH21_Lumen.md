# CH21 Lumen과 간접광

## 무엇인가

Lumen은 UE에서 동적 전역 조명과 반사를 계산하는 시스템입니다. 전역 조명은 표면 사이에서 전달되는 빛을 포함하는 조명이며, Lumen은 변화하는 장면의 간접광과 반사를 실시간으로 근사합니다.

## 렌더링에서 맡는 역할

직접광만으로 설명되지 않는 실내 밝기와 색 번짐, 주변 장면의 반사를 만듭니다. 재질은 같은데 주변 표면이나 광원을 바꾸면 외관이 달라지는 빛 전달을 담당합니다.

## 입력과 출력

입력은 장면의 형상·재질·조명과 카메라 정보입니다. 추적과 조명 조회로 간접광·반사를 구해 표면을 조명하는 데 사용합니다.

## 작동 과정

광원에서 바로 도달한 빛과 다른 표면을 거쳐 온 빛을 구분합니다. 붉은 벽에서 반사된 빛이 흰 벽을 붉게 비추는 것이 간접광의 예입니다.

화면에 있는 정보로 추적을 수행할 수 있고, 화면만으로 부족한 부분은 별도 장면 표현과 지원되는 소프트웨어·하드웨어 추적으로 보완합니다. 화면 밖 물체도 빛 전달에 참여하기 때문입니다.

Surface Cache 같은 표면 표현에서 재질·조명 정보를 조회하고 결과를 갱신·통합합니다. 반사의 조명 평가 방식과 추적 설정은 사용 경로와 품질·비용 조건에 따라 선택합니다.

![간접광의 색 전달](../Images/Concepts/cornellbox.png)

외부 경로 추적 Cornell box 렌더. 색 벽의 간접광 현상을 설명하며 Lumen 실행 결과는 아닙니다. 원본 전체·색상·비율 유지.

[Trevorgoodchild · Public domain · 출처 36](https://commons.wikimedia.org/wiki/File:Cornellbox_pathtracing_irradiancecaching.png)

## 왜 배경 제작에 필요한가

실내 누광·빛 번짐·반사 누락과 재질색을 구분하고 메시 구성·조명 예산을 정할 때 필요합니다. 흰 벽의 붉은 기운을 바로 텍스처에서 상쇄하기 전에 주변 빛 전달을 봅니다.

## 성능과 제작 비용

장면 표현의 갱신, 추적, 조회와 화면 결과의 통합에 비용이 듭니다. 복잡한 장면·변화·품질 설정에 따라 달라지므로 간접광과 반사 관련 작업을 따로 관찰합니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

색 벽만 바꿔 흰 벽의 재질색과 간접광을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part04_LightingAndImageQuality/CH21_Lumen/Maps/L_CH21_Lumen`

### 실습 절차

한쪽 벽만 색이 있는 작은 방과 흰 수신 벽을 준비합니다. Lumen GI와 노출·직접광을 고정합니다. 색 벽의 Base Color만 빨강에서 중성 회색으로 바꾸고 수신 벽의 Base Color와 Lit를 비교합니다.

### 예상 결과와 이유

수신 벽의 Base Color는 유지되고 Lit의 색 번짐은 달라질 것입니다. 직접광은 같아도 주변 재료가 간접 조명을 바꾼다는 예상입니다.

### 결과를 어떻게 해석할까

변화가 없으면 GI 설정과 장면 표현을 먼저 확인합니다. Surface Cache는 추적한 표면의 재질·조명을 조회하는 저장 체계입니다. 누락을 조사할 때 진단하지만 이 장의 첫 결론은 색 번짐의 원인입니다.

## 이 챕터에서 기억할 것

Lumen은 변화하는 장면의 간접광과 반사를 근사합니다. 재질 입력과 주변 장면에서 전달되는 빛을 나눠 이해해야 올바르게 조정할 수 있습니다.

## 이해한 뒤 확인할 조건

반사에서 Surface Cache와 Hit Lighting을 비교하는 것은 별도 문제입니다. 반사 모드나 추적 옵션을 이 간접광 실험과 동시에 바꾸지 않습니다.

## 공식 자료와 확장

- [Lumen Technical Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine)
- [Lumen Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
