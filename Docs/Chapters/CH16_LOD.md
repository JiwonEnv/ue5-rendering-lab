# LOD 멀리서도 남겨야 하는 디테일은 무엇일까

먼 난간의 나사는 보이지 않아도 기둥의 간격과 윗선은 남습니다. 에셋의 모든 면을 같은 비율로 줄이면 이 차이를 놓치기 쉽습니다. LOD는 단순한 폴리곤 감소보다 화면에서 필요한 정보를 고르는 문제입니다.

LOD는 Level of Detail로, 화면에서 필요한 정도에 맞춰 표현의 세부 수준을 바꾸는 방식입니다. 전통적인 Static Mesh LOD는 미리 만든 대체 메시를 선택해 사용합니다.

화면에 거의 기여하지 않는 디테일에 쓰는 작업을 줄이면서 필요한 외관을 유지합니다. 단순히 먼 물체를 대충 만드는 것이 아니라 화면 정보에 자원을 배분하는 원리입니다.

## 거리가 아니라 화면에 남는 크기를 기준으로

단계별 메시와 화면 크기 조건에 따라 사용할 표현이 선택됩니다. 물체의 실제 크기와 카메라 시야각도 화면 점유율을 바꾸므로 거리 하나만으로 세부를 정하지 않습니다.

원본을 기준으로 작은 부품과 면을 줄인 대체 표현을 준비합니다. 실루엣·큰 간격·그림자에 중요한 형태를 먼저 구분합니다. 렌더러가 화면 점유율 등의 기준으로 표현 단계를 선택합니다. 같은 거리라도 큰 물체와 작은 물체 또는 다른 FOV에서는 필요한 디테일이 다릅니다. 카메라 이동으로 단계가 바뀝니다. 두 표현의 윤곽·노멀·재질 차이가 크면 전환 순간 튀므로 정지 외관뿐 아니라 이동과 그림자도 확인합니다.

![외부 LOD 그림에서는 단순화에 따라 윤곽이 각지게 바뀝니다. 원본의 LOD 1·2·3 표기는 UE에서 흔히 시작하는 LOD0 번호와 다릅니다.](../Images/External/lod-print.png)

외부 LOD 그림에서는 단순화에 따라 윤곽이 각지게 바뀝니다. 원본의 LOD 1·2·3 표기는 UE에서 흔히 시작하는 LOD0 번호와 다릅니다.

[Sirotk · Wikimedia Commons · 출처 42](https://commons.wikimedia.org/wiki/File:LOD_Example.png)

원본 전체와 비율 유지

[이용 조건 CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## 나사를 없애도 윤곽은 남겨야 한다

난간의 나사와 베벨, 먼 건물의 장식처럼 플레이 거리에서 읽히지 않는 부분을 줄일 때 필요합니다. 비율로 일괄 감소하기보다 남길 시각 정보를 먼저 정합니다.

카메라가 멀어지면 작은 베벨과 나사는 몇 픽셀 안으로 사라집니다. 반면 상단 실루엣을 크게 바꾸면 전환 순간 건물의 형태가 튈 수 있습니다. 단순화의 우선순위는 부품의 실제 크기보다 플레이 화면에서 맡는 역할에 달려 있습니다.

## 줄인 삼각형이 전체 시간을 줄이는 조건

정점·삼각형·섹션과 재질을 줄일 수 있지만 픽셀 비용이 같으면 총 이득은 작을 수 있습니다. 전환 중 두 표현이 처리되는 조건도 별도로 확인합니다.

좋은 LOD는 원본을 균등하게 덜어낸 형상이 아니라 멀리서 읽힐 정보를 남긴 표현입니다. 화면 크기와 이동 중 전환을 기준으로 보면 무엇을 생략할지 더 분명해집니다.

## 참고 자료

- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Optimizing LOD Screen Size Per Platform](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-lod-screen-size-per-platform-in-unreal-engine)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
