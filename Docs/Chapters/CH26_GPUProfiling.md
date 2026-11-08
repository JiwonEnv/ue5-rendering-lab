# CH26 GPU Profiler와 개선 검증

## 중심 질문

무거운 GPU 패스를 찾은 다음 어떻게 수정 효과를 증명할까?

## 먼저 알아둘 답

같은 조건에서 한 원인만 바꾸고, 해당 패스·전체 프레임·화질이 함께 어떻게 달라졌는지 확인합니다.

## 왜 알아야 할까

진단 도구의 숫자를 실제 제작 결정과 재현 가능한 개선 기록으로 연결하기 위해 배웁니다.

### 예제 학습 목표

하나의 가설을 변경·복원하며 패스 감소와 총 프레임 개선을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part05_Profiling/CH26_GPUProfiling/Maps/L_CH26_GPUProfiling`

## 왜 이런 결과가 생길까

GPU Profiler는 작업 시간을 이벤트와 렌더 패스별로 보여 줍니다. 큰 구간 안에 세부 구간이 들어 있으므로 부모와 자식 시간을 더하면 중복할 수 있습니다. 무거운 패스를 찾은 뒤 어떤 에셋·기능이 그 일을 만드는지 가설을 세웁니다. 패스 이름만 보고 모든 그림자나 모든 반투명을 제거하는 것은 원인 검증이 아닙니다.

## 제작 중에는 이렇게 나타납니다

패스가 빨라져도 CPU나 다른 GPU 일이 제한하면 전체 프레임은 그대로일 수 있습니다. 반대로 시간을 줄이면서 필요한 외관을 잃었다면 목표를 만족한 개선으로 볼 수 없습니다.

![외부 실제 도구 화면 · GPU Insights 시간축의 이벤트 계층을 발췌·확대했습니다.](../Images/External/gpu-events-print.png)

외부 실제 도구 화면 · GPU Insights 시간축의 이벤트 계층을 발췌·확대했습니다.

읽을 곳  큰 Frame 구간 안에 작은 작업 구간이 포함됩니다. 로그에서 Inclusive는 하위 작업을 포함한 시간, Exclusive는 자체 시간입니다. 부모·자식 시간을 모두 더하지 않습니다. UE 5.6 예시이므로 실제 UI와 기록 항목은 현재 빌드에서 확인합니다.

[Tom Looman 문서 수록 · Unreal Engine 도구 화면 · 출처 60](https://tomlooman.com/unreal-engine-5-6-performance-highlights/)

원본 일부 발췌·확대 · 색상 유지 · 표제 추가

원저작권과 원문 출처 표시는 유지합니다

## 실습 절차

CH25에서 GPU 제한을 확인한 구간을 씁니다. 예를 들어 풀의 WPO가 그림자 갱신을 늘린다는 가설을 세우고 WPO만 끕니다. 동일 경로를 워밍업 뒤 세 번씩 기록하고 원래 설정으로 돌려 재현성을 확인합니다.

## 예상 결과와 이유

가설이 맞으면 그림자 생성 구간이 줄고, GPU 제한이 충분하면 총 시간도 줄 것입니다. 동시에 움직이는 풀과 그림자의 외관 차이가 남을 것입니다.

## 결과를 어떻게 해석할까

해당 구간만 줄었으면 국소 효과를 확인한 것입니다. 전체 시간이 그대로면 다음 제한 원인을 조사합니다. 변화가 반복되지 않으면 셰이더 준비·로딩·측정 흔들림을 먼저 확인합니다.

## 실제 제작에서의 선택

변경 이유, 유지한 조건, 전후 시간, 외관 손실, 채택 여부를 함께 남깁니다. 실제 제품의 목표를 만족한 변경만 채택합니다.

## 이해한 뒤 확인할 조건

이벤트 표시와 캡처 방법은 UE 버전에 따라 다릅니다. stat gpu로 큰 범위를 보고 profilegpu 또는 Unreal Insights로 좁히며, 중첩·동시 실행 시간을 단순 합산하지 않습니다.

## 공식 자료와 확장

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)
- [Beyond Print String · GPU Profiler](https://dev.epicgames.com/community/learning/talks-and-demos/WDmB/beyond-print-string-debugging-unreal-engine-lightning-round)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
