# Fresnel 물과 유리의 반사가 각도에 따라 달라지는 이유

물웅덩이를 위에서 내려다볼 때와 낮은 시선으로 볼 때 반사의 비중은 다릅니다. 같은 표면인데도 보는 방향에 따라 인상이 달라지는 데에는 Fresnel이라는 경계면의 빛 반응이 관여합니다.

Fresnel은 두 물질의 경계에서 반사되는 빛의 비율이 각도와 물질 특성에 따라 달라지는 현상입니다. 일반 비금속 경계에서는 스치는 각도에서 반사가 강해지는 반응이 대표적입니다.

BRDF와 투과 모델 안에서 반사와 투과의 비중을 정하는 데 쓰입니다. 물·유리·코팅이 보는 각도에 따라 다르게 보이는 물리적 근거입니다.

## 경계에서 반사되는 빛의 비율

물질 경계의 특성과 입사각이 반사율을 바꿉니다. 이 반사율은 광원과 환경, 거칠기와 함께 작용하므로 각도 반응 하나만으로 화면의 밝기를 모두 설명할 수는 없습니다.

정면과 비스듬한 입사의 반사율을 구분합니다. F0는 정면 입사에서의 반사율로, 물질 경계의 특성을 표현하는 기준 중 하나입니다. 각도 변화에 따른 반사율을 계산해 표면 반응에 반영합니다. 거친 표면에서는 미세면 방향들이 섞이므로 단순한 화면 가장자리 선 하나로 나타나는 현상은 아닙니다. 렌더러가 반사할 환경과 빛을 결합합니다. 한편 UE의 Fresnel 노드는 시선과 표면 방향으로 마스크를 만들 수 있어, 물리 반사 외의 림 효과에도 사용됩니다.

![외부 Fresnel 마스크는 각도 의존성을 이해하는 데 쓰는 표현입니다. 발광에 연결한 마스크와 물질의 실제 반사율은 구분됩니다.](../Images/External/fresnel-print.png)

외부 Fresnel 마스크는 각도 의존성을 이해하는 데 쓰는 표현입니다. 발광에 연결한 마스크와 물질의 실제 반사율은 구분됩니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 41](https://learnopengl.com/PBR/Theory)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 물리 반사와 가장자리 발광을 구분하기

물과 유리의 반사를 자연스럽게 조정하거나, 별도의 가장자리 발광을 설계할 때 필요합니다. 기본 PBR 반사에 포함된 각도 반응과 추가한 아트 효과를 구분해야 중복 보정을 피할 수 있습니다.

PBR 반사에는 이미 각도에 따른 반응이 포함됩니다. 여기에 Fresnel 노드를 발광으로 더하면 반사율을 조절하는 것과 다른 연출이 됩니다. 주변 환경이 어두워도 가장자리가 밝아질 수 있기 때문에, 두 효과는 비슷해 보여도 빛을 만드는 원인이 다릅니다.

## 유리 전체의 비용을 마스크 하나로 설명할 수는 없다

기본 재질의 각도 반응과 추가 텍스처·발광·반투명 기능의 비용은 다릅니다. Fresnel 노드 하나의 외관을 전체 유리 렌더링 비용과 동일시하지 않습니다.

Fresnel을 이해하면 각도에 따라 달라지는 자연스러운 반사와 의도적으로 추가한 림 효과를 구분할 수 있습니다. 물과 유리의 재료감은 가장자리에 밝은 선을 넣는 것보다 더 넓은 관계 속에 있습니다.

## 참고 자료

- [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)
- [Using Fresnel](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-fresnel-in-your-unreal-engine-materials)
- [Overview of Substrate Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
