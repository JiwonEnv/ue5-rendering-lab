# CH25 CPU와 GPU 병목

## 중심 질문

폴리곤과 해상도를 줄였는데 왜 FPS가 그대로일까?

## 먼저 알아둘 답

프레임 진행을 제한하는 다른 작업이 남아 있으면 일부 GPU 일을 줄여도 최종 속도는 오르지 않을 수 있습니다.

## 왜 알아야 할까

최적화 대상을 추측으로 고르지 않고 실제로 프레임을 제한하는 구간부터 수정하기 위해 배웁니다.

### 예제 학습 목표

내부 해상도 변화에 Frame과 GPU 시간이 함께 반응하는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part05_Profiling/CH25_CPUGPUBottlenecks/Maps/L_CH25_CPUGPUBottlenecks`

## 왜 이런 결과가 생길까

CPU는 게임 상태와 그리기 명령을 준비하고 GPU는 제출된 작업을 실행합니다. 이 작업은 여러 프레임에 걸쳐 겹칠 수 있습니다. 처리율은 느린 준비·실행 구간이나 동기화에 제한됩니다. 병목은 이 제한 원인입니다. CPU가 명령을 늦게 주면 GPU가 가벼워져도 다음 프레임 준비가 빨라지지는 않습니다.

## 제작 중에는 이렇게 나타납니다

최적화는 눈에 복잡한 물체를 줄이는 일과 같지 않습니다. 프레임 제한이나 VSync로 기다리는 조건이라면 계산을 줄여도 표시 FPS가 유지될 수 있습니다.

![외부 실측 화면 · John Farrow가 기록한 Unreal Insights의 프레임 시간 그래프입니다.](../Images/External/cpu-frames-print.png)

외부 실측 화면 · John Farrow가 기록한 Unreal Insights의 프레임 시간 그래프입니다.

읽을 곳  긴 막대가 나타난 구간을 고른 뒤 CPU·GPU 시간축을 열어 원인을 찾습니다. 그래프 자체로 CPU 병목이라고 판정하지 않습니다. 저자의 2024년 프로젝트 예시이며 이 저장소의 측정 결과가 아닙니다.

[© John Farrow · Unrealcode.net · 출처 59](https://www.unrealcode.net/Optimization_Part3/)

원본 전체 유지 · 투명 배경은 흰색으로 표시

원저작권과 원문 출처 표시는 유지합니다

## 실습 절차

진단용으로 프레임 제한과 VSync 영향을 확인합니다. 같은 경로의 안정 구간에서 stat unit의 Frame·Game·Draw·GPU를 기록한 뒤 내부 해상도만 낮춰 다시 비교합니다.

## 예상 결과와 이유

GPU 화면 계산이 제한 원인이면 해상도 감소에 GPU와 Frame이 함께 반응할 수 있습니다. CPU 제한이면 GPU는 줄어도 Frame 변화가 작을 수 있습니다.

## 결과를 어떻게 해석할까

이는 원인 후보를 좁히는 실험입니다. 가장 긴 수치가 대기 시간을 포함할 수도 있으므로 Unreal Insights에서 Game·Render·RHI·GPU 시간축을 대조해 계산과 기다림을 구분합니다.

## 실제 제작에서의 선택

GPU가 원인이면 무거운 패스로, CPU가 원인이면 게임 로직·명령 준비·관리 작업으로 조사 방향을 정합니다.

## 이해한 뒤 확인할 조건

FPS 대신 ms도 기록합니다. 프레임 제한을 풀어 원인을 진단한 뒤 실제 제품 설정으로 되돌려 효과를 확인합니다.

## 공식 자료와 확장

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
