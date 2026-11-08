# GPU Profiler 프레임의 비용을 읽는 법

프레임이 느리다는 사실과 무엇을 고쳐야 하는지는 다른 정보입니다. GPU Profiler는 표면·그림자·반투명·후처리 같은 작업의 시간을 드러내지만, 그 비용을 만드는 제작 원인까지 자동으로 결정해 주지는 않습니다.

GPU Profiler는 GPU 작업을 이벤트와 렌더 패스별 시간으로 관찰하는 도구입니다. 프로파일링은 실행 중 어디에 시간이 쓰이는지 측정하고 원인 후보를 좁히는 과정입니다.

느린 프레임을 구성하는 작업을 찾아 아트 변경의 가설과 연결합니다. 도구는 비용의 위치를 보여 주며, 어떤 제작 선택이 원인인지는 비교 실험으로 검증합니다.

## 패스와 이벤트로 드러나는 GPU의 일

GPU 캡처의 이벤트와 시간 정보는 패스의 계층과 시간축으로 드러납니다. 다른 조건의 실행과 비교할 때도 각 구간이 무엇을 포함하는지 알아야 숫자를 같은 의미로 읽을 수 있습니다.

stat gpu는 큰 GPU 작업 묶음을, 지원되는 profilegpu와 Unreal Insights는 더 세부적인 시간과 이벤트를 보여 줍니다. 그림자·표면·반투명·후처리가 프레임 안에서 차지하는 위치를 읽는 정보입니다. 부모 이벤트와 세부 구간을 펼쳐 어느 작업이 시간을 쓰는지 찾습니다. 포함 시간과 자체 시간을 구분하고 겹쳐 실행된 작업을 단순 합산하지 않습니다. 이벤트의 비용은 그것을 만드는 에셋과 기능에 대한 설명으로 이어져야 합니다. 같은 조건의 반복 결과와 해당 패스·전체 프레임·외관의 관계가 있어야 일시적인 숫자 변화와 유효한 개선을 구분할 수 있습니다.

![원문 UE 5.6 사례의 외부 GPU Insights 이벤트 계층입니다. 부모 구간 안에 자식이 포함되므로 모든 시간을 단순히 더하면 중복할 수 있습니다.](../Images/External/gpu-events-print.png)

원문 UE 5.6 사례의 외부 GPU Insights 이벤트 계층입니다. 부모 구간 안에 자식이 포함되므로 모든 시간을 단순히 더하면 중복할 수 있습니다.

[Tom Looman 문서 수록 · Unreal Engine 도구 화면 · 출처 60](https://tomlooman.com/unreal-engine-5-6-performance-highlights/)

원본 일부 발췌·확대 · 색상 유지 · 표제 추가

원저작권과 원문 출처 표시는 유지합니다

## 그림자 시간이 길다는 말만으로 풀을 지울 수는 없다

풀의 그림자 갱신, 큰 반투명, 복잡한 머티리얼 등 제작 변경의 채택 여부를 정할 때 필요합니다. 빠른 한 번의 숫자보다 재현성과 필요한 품질을 유지했는지가 중요합니다.

풀의 변형이 그림자 페이지 갱신을 늘린다면 그림자 구간의 비용과 연결됩니다. 그렇더라도 움직임을 없애는 변경이 제품에 맞는지는 별개입니다. 비용의 위치를 찾는 정보와, 필요한 외관을 유지하며 바꿀 대상을 정하는 판단 사이에는 원인에 대한 설명이 필요합니다.

## 숫자의 감소가 개선이 되는 조건

캡처·셰이더 준비·로딩 순간은 측정을 흔들 수 있습니다. 안정 구간을 쓰고 대상 기기의 실제 프레임을 확인합니다. 도구의 표시 방식은 UE 버전에 따라 달라집니다.

프로파일러는 어떤 일이 무거운지 보여 주는 지도입니다. 제작의 결정은 그 일이 생기는 이유와 필요한 화면의 가치를 함께 읽을 때 가능해집니다. 패스 하나의 감소보다 실제 목표를 만족하는 변화가 중요합니다.

## 참고 자료

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)
- [Beyond Print String · GPU Profiler](https://dev.epicgames.com/community/learning/talks-and-demos/WDmB/beyond-print-string-debugging-unreal-engine-lightning-round)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
