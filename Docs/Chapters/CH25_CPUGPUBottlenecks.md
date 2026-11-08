# CH25 CPU와 GPU 병목

## 무엇인가

병목은 프레임의 처리율이나 완료 시간을 제한하는 작업 또는 대기 관계입니다. CPU와 GPU 병목 분석은 어느 쪽의 준비·실행이 실제로 프레임 진행을 제한하는지 찾는 과정입니다.

## 렌더링에서 맡는 역할

효과가 있는 최적화 대상의 우선순위를 정합니다. 눈에 복잡한 에셋을 줄이는 것과 프레임을 제한하는 일을 줄이는 것은 같지 않으므로 먼저 제한 원인을 확인합니다.

## 입력과 출력

입력은 반복 가능한 실행 구간과 CPU·GPU·프레임 시간 및 타임라인입니다. 결과는 계산·제출·동기화·로딩 중 어느 작업이 제한 후보인지에 대한 판단입니다.

## 작동 과정

CPU의 게임 상태 갱신과 명령 준비, GPU의 실행은 여러 프레임에서 겹칠 수 있습니다. 단순히 모든 시간을 더해서 프레임 시간을 구하지 않습니다.

stat unit 등으로 Frame·Game·Draw·GPU를 살펴 큰 방향을 정합니다. 프레임 제한과 VSync가 만든 대기라면 계산을 줄여도 FPS가 유지될 수 있습니다.

해상도 같은 영향 범위가 알려진 변수를 바꾸고 반응을 봅니다. 이어 타임라인에서 계산과 기다림, 작업 의존 관계를 확인해 원인을 좁힙니다.

![외부 실측 화면 · John Farrow가 기록한 Unreal Insights의 프레임 시간 그래프입니다.](../Images/External/cpu-frames-print.png)

외부 실측 화면 · John Farrow가 기록한 Unreal Insights의 프레임 시간 그래프입니다.

읽을 곳  긴 막대가 나타난 구간을 고른 뒤 CPU·GPU 시간축을 열어 원인을 찾습니다. 그래프 자체로 CPU 병목이라고 판정하지 않습니다. 저자의 2024년 프로젝트 예시이며 이 저장소의 측정 결과가 아닙니다.

[© John Farrow · Unrealcode.net · 출처 59](https://www.unrealcode.net/Optimization_Part3/)

원본 전체 유지 · 투명 배경은 흰색으로 표시

원저작권과 원문 출처 표시는 유지합니다

## 왜 배경 제작에 필요한가

폴리곤과 재질을 줄여도 FPS가 그대로일 때, 첫 진입만 끊길 때, CPU 제출이 무거운 대규모 배치에서 필요합니다. 수정할 에셋인지 실행·관리 구조인지 조사 방향을 정합니다.

## 성능과 제작 비용

GPU만 가벼워져도 CPU가 제한하면 총 프레임은 거의 그대로일 수 있습니다. 가장 긴 막대도 대기를 포함할 수 있어 실제로 제한하는 관계를 확인해야 합니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

내부 해상도 변화에 Frame과 GPU 시간이 함께 반응하는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part05_Profiling/CH25_CPUGPUBottlenecks/Maps/L_CH25_CPUGPUBottlenecks`

### 실습 절차

진단용으로 프레임 제한과 VSync 영향을 확인합니다. 같은 경로의 안정 구간에서 stat unit의 Frame·Game·Draw·GPU를 기록한 뒤 내부 해상도만 낮춰 다시 비교합니다.

### 예상 결과와 이유

GPU 화면 계산이 제한 원인이면 해상도 감소에 GPU와 Frame이 함께 반응할 수 있습니다. CPU 제한이면 GPU는 줄어도 Frame 변화가 작을 수 있습니다.

### 결과를 어떻게 해석할까

이는 원인 후보를 좁히는 실험입니다. 가장 긴 수치가 대기 시간을 포함할 수도 있으므로 Unreal Insights에서 Game·Render·RHI·GPU 시간축을 대조해 계산과 기다림을 구분합니다.

## 이 챕터에서 기억할 것

병목 분석은 가장 복잡한 물체가 아니라 프레임을 제한하는 일을 찾는 과정입니다. 부분 최적화와 전체 개선을 구분합니다.

## 이해한 뒤 확인할 조건

FPS 대신 ms도 기록합니다. 프레임 제한을 풀어 원인을 진단한 뒤 실제 제품 설정으로 되돌려 효과를 확인합니다.

## 공식 자료와 확장

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
