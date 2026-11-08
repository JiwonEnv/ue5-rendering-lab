# CH09 Fresnel과 시선 각도

## 중심 질문

물이나 유리는 왜 비스듬히 볼 때 반사가 강해질까?

## 먼저 알아둘 답

반사되는 빛의 비율은 입사각에 따라 달라지며, 비금속은 스치는 각도에서 반사가 강해집니다.

## 왜 알아야 할까

물·유리·코팅의 각도별 외관을 만들고 물리 반사와 의도적인 림 효과를 구분하기 위해 배웁니다.

### 예제 학습 목표

각도 의존 반사와 Fresnel 발광 마스크의 차이를 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH09_Fresnel/Maps/L_CH09_Fresnel`

## 왜 이런 결과가 생길까

Fresnel은 경계면에서 빛이 얼마나 반사되는지 각도와 물질 특성에 따라 설명합니다. 표면을 정면에서 보는 조건과 거의 스치듯 보는 조건의 반사율이 같지 않습니다. 실제 화면에서는 광원의 분포와 거칠기도 함께 작용하므로 가장자리가 언제나 밝은 선으로 보인다는 뜻은 아닙니다.

## 제작 중에는 이렇게 나타납니다

PBR 재질의 반사에는 이미 각도 의존성이 포함됩니다. 여기에 Fresnel 노드를 Emissive로 더하면 물리 반사뿐 아니라 광원 없이도 밝아지는 별도의 연출을 만든 것입니다.

![외부 시각화 이미지 · 구의 중심과 실루엣 부근에서 Fresnel 반사 계수가 달라지는 예입니다.](../Images/External/fresnel-print.png)

외부 시각화 이미지 · 구의 중심과 실루엣 부근에서 Fresnel 반사 계수가 달라지는 예입니다.

읽을 곳  중심보다 테두리가 밝습니다. 곡면의 테두리에서 시선이 표면에 더 비스듬하게 닿기 때문입니다. 물체의 완성 렌더가 아닌 반사 계수의 시각화입니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 41](https://learnopengl.com/PBR/Theory)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 실습 절차

반사할 환경이 있는 물 또는 유리 표면을 준비합니다. 카메라 각도만 바꿔 정면과 낮은 시점의 반사를 봅니다. 이후 별도 재질에 Fresnel 노드의 출력을 Emissive에 연결하고 조명을 줄여 비교합니다.

## 예상 결과와 이유

기본 표면에서는 각도에 따라 환경 반사의 비중이 달라질 것입니다. 발광 마스크는 환경이 어두워져도 스치는 부분을 밝힐 수 있습니다.

## 결과를 어떻게 해석할까

두 결과가 비슷해 보여도 빛을 만드는 원인이 다릅니다. Fresnel 노드의 마스크를 실제 물질의 반사율 전체와 동일시하지 않습니다.

## 실제 제작에서의 선택

자연스러운 유리·물은 기본 반사 모델과 거칠기부터 맞추고, 림 발광은 필요한 연출로 명시해 추가합니다.

## 이해한 뒤 확인할 조건

F0는 정면 입사에서의 반사율입니다. 굴절률과 금속의 파장별 반응 같은 세부는 공식 PBR 자료에서 확장합니다.

## 공식 자료와 확장

- [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)
- [Using Fresnel](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-fresnel-in-your-unreal-engine-materials)
- [Overview of Substrate Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
