# GBuffer 최종 색 뒤에 있는 표면 정보

벽이 지나치게 번들거리면 라이트를 약하게 만들고 싶어집니다. 하지만 거칠기 입력이 잘못됐다면 조명으로 보정한 결과는 다른 환경에서 다시 무너집니다. 최종 화면 뒤의 재질 정보를 따로 볼 수 있게 해 주는 것이 GBuffer입니다.

GBuffer는 Deferred 조명이 사용할 표면 특성을 화면 위치별로 저장하는 버퍼 묶음입니다. 버퍼는 계산에 쓸 데이터를 보관하는 메모리이며, GBuffer는 최종 사진이 아닌 표면 정보의 중간 저장소입니다.

표면의 기본 색과 방향·거칠기를 조명 계산과 분리합니다. 이 데이터를 기록한 뒤 여러 조명과 후속 계산이 재사용할 수 있습니다. 재질 입력과 조명 결과를 따로 진단할 수 있는 이유도 여기에 있습니다.

## 빛을 계산하기 전에 남겨 두는 데이터

텍스처와 재질이 만든 표면값은 해당 화면 위치의 데이터로 남습니다. 조명은 깊이와 카메라, 광원 정보와 함께 이 값을 읽어 최종 표면색을 계산합니다.

표면을 그리는 Base Pass에서 텍스처와 재질 입력을 평가합니다. Base Color는 기본 표면색, Roughness는 반사 분포의 거칠기, 법선은 표면 방향을 나타냅니다. 계산한 속성을 정해진 형식으로 저장합니다. Scene Depth는 별도의 깊이 정보입니다. 모든 속성이 각각 독립된 이미지 하나에 저장되는 것은 아니며, 채널 배치는 렌더러와 저장 형식에 따라 달라집니다. 조명 단계가 저장한 값을 읽고 빛의 방향·세기와 표면 반응을 결합합니다. 같은 표면 데이터도 조명이 바뀌면 최종 색이 달라집니다. Buffer Visualization은 일부 정보를 관찰용으로 표시합니다.

![최종 조명색 대신 표면 속성을 따로 표시한 외부 GBuffer 사례입니다. 진단 화면의 색 배치는 실제 저장 채널 배열을 그대로 보여 주는 것은 아닙니다.](../Images/External/gbuffer-print.png)

최종 조명색 대신 표면 속성을 따로 표시한 외부 GBuffer 사례입니다. 진단 화면의 색 배치는 실제 저장 채널 배열을 그대로 보여 주는 것은 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 39](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 반짝이는 벽을 조명만으로 고치기 어려운 이유

벽의 번들거림은 Roughness, 반사의 방향 오류는 World Normal, 고정된 색 얼룩은 Base Color부터 확인할 수 있습니다. 진단이 의도와 다르면 재질 입력을, 입력이 맞으면 조명과 반사 환경을 조사합니다.

같은 벽의 거칠기가 낮아지면 반사가 좁고 선명하게 보일 수 있습니다. 이때 Base Color가 같아도 Lit의 인상은 달라집니다. 반대로 광원만 움직이면 표면의 기본 값이 그대로인 상태에서 밝은 부분의 위치가 바뀝니다. 두 변화는 최종 색만으로는 쉽게 뒤섞입니다.

## 중간 정보를 저장하는 데도 비용이 든다

저장할 화면 픽셀 수와 픽셀당 데이터가 메모리 사용과 대역폭을 좌우합니다. 머티리얼 노드 수가 많아졌다는 사실만으로 GBuffer의 바이트 수가 같은 비율로 늘지는 않습니다.

GBuffer는 최종 화면을 한 번 더 찍은 사진이 아니라 조명이 읽는 표면 데이터입니다. 이 차이를 이해하면 재질을 고칠 문제와 빛을 고칠 문제를 같은 밝기 조절로 처리하지 않게 됩니다.

## 참고 자료

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
