# CH16 LOD와 화면 크기

## 중심 질문

먼 난간의 나사는 왜 생략해도 되지만 윤곽은 남겨야 할까?

## 먼저 알아둘 답

화면에서 읽히지 않는 디테일은 줄이고, 적은 픽셀에서도 보이는 형태 정보는 유지해야 합니다.

## 왜 알아야 할까

에셋의 디테일을 플레이 거리와 출력 크기에 맞게 배분하기 위해 배웁니다.

### 예제 학습 목표

카메라 이동에서 LOD가 잃는 디테일과 남겨야 할 윤곽을 판정합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH16_LOD/Maps/L_CH16_LOD`

## 왜 이런 결과가 생길까

LOD는 필요한 세부 수준에 따라 표현을 바꾸는 방식입니다. 전통 Static Mesh LOD는 미리 만든 대체 메시를 선택합니다. 멀어질수록 같은 형상이 차지하는 픽셀이 줄어 작은 나사는 보이지 않지만, 기둥의 굵기나 상단 실루엣은 여전히 외관을 좌우합니다. 따라서 원본의 모든 부분을 같은 비율로 줄이는 것이 좋은 단순화는 아닙니다.

## 제작 중에는 이렇게 나타납니다

UE는 화면 크기를 기준으로 LOD를 선택할 수 있습니다. 거리뿐 아니라 메시 크기와 카메라 시야각인 FOV도 화면 점유율을 바꾸므로 같은 거리에서 항상 같은 LOD가 나오는 것은 아닙니다.

![외부 비교 그림 · 비슷한 실루엣을 더 적은 변으로 근사한 세 가지 LOD입니다.](../Images/External/lod-print.png)

외부 비교 그림 · 비슷한 실루엣을 더 적은 변으로 근사한 세 가지 LOD입니다.

읽을 곳  오른쪽으로 갈수록 위쪽 윤곽이 각지게 바뀝니다. 원본의 LOD 1·2·3 표기는 해당 그림의 번호이며 UE에서 흔히 시작하는 LOD0 번호와 구별합니다.

[Sirotk · Wikimedia Commons · 출처 42](https://commons.wikimedia.org/wiki/File:LOD_Example.png)

원본 전체와 비율 유지

[이용 조건 CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## 실습 절차

난간의 원본과 나사·작은 베벨을 줄인 LOD를 준비합니다. 같은 구도에서 강제 LOD로 외관을 비교한 뒤, Screen Size 전환을 켜고 카메라를 천천히 이동합니다.

## 예상 결과와 이유

먼 구도에서는 작은 부품의 차이가 줄어들지만 실루엣을 많이 바꾸면 전환 순간 형태가 튈 것입니다. 가까운 구도에서는 단순화 손실이 더 잘 보일 것입니다.

## 결과를 어떻게 해석할까

정지 비교에서 비슷해도 이동 중 전환과 그림자 변화를 확인합니다. 줄인 삼각형 수가 아니라 잃은 시각 정보가 허용되는지를 먼저 판단합니다.

## 실제 제작에서의 선택

실루엣·큰 간격·그림자 형태를 보존하고 작은 면부터 줄입니다. 이후 GPU 시간이 줄었는지 확인해 실제 병목과 연결합니다.

## 이해한 뒤 확인할 조건

픽셀 재질이 병목이면 삼각형 감소만으로 전체 이득이 작을 수 있습니다. 디더 전환과 재질 단순화는 다음 단계의 선택입니다.

## 공식 자료와 확장

- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Optimizing LOD Screen Size Per Platform](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-lod-screen-size-per-platform-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
