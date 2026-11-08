# CH26 GPU Profiler와 개선 검증

## 무엇인가

GPU Profiler는 GPU 작업을 이벤트와 렌더 패스별 시간으로 관찰하는 도구입니다. 프로파일링은 실행 중 어디에 시간이 쓰이는지 측정하고 원인 후보를 좁히는 과정입니다.

## 렌더링에서 맡는 역할

느린 프레임을 구성하는 작업을 찾아 아트 변경의 가설과 연결합니다. 도구는 비용의 위치를 보여 주며, 어떤 제작 선택이 원인인지는 비교 실험으로 검증합니다.

## 입력과 출력

입력은 캡처한 프레임의 GPU 이벤트와 시간 정보입니다. 출력은 계층·시간축·패스별 비용으로, 다른 조건의 실행과 비교해 효과를 판정합니다.

## 작동 과정

stat gpu 등으로 큰 비용 범위를 찾고 지원되는 profilegpu·Unreal Insights로 세부를 봅니다. 프레임의 전체 구조 안에서 그림자·표면·반투명·후처리 등을 구분합니다.

부모 이벤트와 세부 구간을 펼쳐 어느 작업이 시간을 쓰는지 찾습니다. 포함 시간과 자체 시간을 구분하고 겹쳐 실행된 작업을 단순 합산하지 않습니다.

작업을 늘리는 에셋·기능에 가설을 세워 한 변수만 바꿉니다. 같은 조건으로 반복 측정하고 해당 패스·전체 프레임·외관이 함께 어떻게 달라졌는지 기록합니다.

![외부 실제 도구 화면 · GPU Insights 시간축의 이벤트 계층을 발췌·확대했습니다.](../Images/External/gpu-events-print.png)

외부 실제 도구 화면 · GPU Insights 시간축의 이벤트 계층을 발췌·확대했습니다.

읽을 곳  큰 Frame 구간 안에 작은 작업 구간이 포함됩니다. 로그에서 Inclusive는 하위 작업을 포함한 시간, Exclusive는 자체 시간입니다. 부모·자식 시간을 모두 더하지 않습니다. UE 5.6 예시이므로 실제 UI와 기록 항목은 현재 빌드에서 확인합니다.

[Tom Looman 문서 수록 · Unreal Engine 도구 화면 · 출처 60](https://tomlooman.com/unreal-engine-5-6-performance-highlights/)

원본 일부 발췌·확대 · 색상 유지 · 표제 추가

원저작권과 원문 출처 표시는 유지합니다

## 왜 배경 제작에 필요한가

풀의 그림자 갱신, 큰 반투명, 복잡한 머티리얼 등 제작 변경의 채택 여부를 정할 때 필요합니다. 빠른 한 번의 숫자보다 재현성과 필요한 품질을 유지했는지가 중요합니다.

## 성능과 제작 비용

캡처·셰이더 준비·로딩 순간은 측정을 흔들 수 있습니다. 안정 구간을 쓰고 대상 기기의 실제 프레임을 확인합니다. 도구의 표시 방식은 UE 버전에 따라 달라집니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

하나의 가설을 변경·복원하며 패스 감소와 총 프레임 개선을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part05_Profiling/CH26_GPUProfiling/Maps/L_CH26_GPUProfiling`

### 실습 절차

CH25에서 GPU 제한을 확인한 구간을 씁니다. 예를 들어 풀의 WPO가 그림자 갱신을 늘린다는 가설을 세우고 WPO만 끕니다. 동일 경로를 워밍업 뒤 세 번씩 기록하고 원래 설정으로 돌려 재현성을 확인합니다.

### 예상 결과와 이유

가설이 맞으면 그림자 생성 구간이 줄고, GPU 제한이 충분하면 총 시간도 줄 것입니다. 동시에 움직이는 풀과 그림자의 외관 차이가 남을 것입니다.

### 결과를 어떻게 해석할까

해당 구간만 줄었으면 국소 효과를 확인한 것입니다. 전체 시간이 그대로면 다음 제한 원인을 조사합니다. 변화가 반복되지 않으면 셰이더 준비·로딩·측정 흔들림을 먼저 확인합니다.

## 이 챕터에서 기억할 것

GPU Profiler는 무거운 일을 찾는 도구이며, 개선은 동일 조건의 변경·복원 실험으로 증명합니다. 패스 감소와 전체 제품 목표 달성을 구분합니다.

## 이해한 뒤 확인할 조건

이벤트 표시와 캡처 방법은 UE 버전에 따라 다릅니다. stat gpu로 큰 범위를 보고 profilegpu 또는 Unreal Insights로 좁히며, 중첩·동시 실행 시간을 단순 합산하지 않습니다.

## 공식 자료와 확장

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)
- [Beyond Print String · GPU Profiler](https://dev.epicgames.com/community/learning/talks-and-demos/WDmB/beyond-print-string-debugging-unreal-engine-lightning-round)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
