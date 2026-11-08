# CH07 PBR과 재질 입력

## 중심 질문

조명을 바꿔도 금속과 페인트가 재료답게 보이려면 무엇을 입력해야 할까?

## 먼저 알아둘 답

재료의 고유 반응을 입력하고, 장면의 빛과 그림자는 조명 계산에 맡겨야 합니다.

## 왜 알아야 할까

한 조명에서만 그럴듯한 텍스처 대신 여러 환경에 쓸 수 있는 배경 재질을 만들기 위해 배웁니다.

### 예제 학습 목표

금속성·거칠기 입력과 광원 이동의 역할을 나누어 관찰합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH07_PBR/Maps/L_CH07_PBR`

## 왜 이런 결과가 생길까

PBR은 빛과 물질의 상호작용을 물리적으로 그럴듯하게 근사하는 제작 방식입니다. 비금속의 Base Color는 주로 확산 반사의 색을, 금속의 Base Color는 금속 반사의 색을 정합니다. Metallic은 어느 재료 반응을 사용할지, Roughness는 반사가 얼마나 퍼질지 정합니다. 이 반응에 장면의 빛이 들어와 최종 외관이 생깁니다.

## 제작 중에는 이렇게 나타납니다

텍스처에 특정 광원의 하이라이트나 방향성 그림자를 그려 넣으면, 라이트가 움직여도 그 흔적이 남습니다. 도장과 벗겨진 철은 밝고 어두운 정도만 다른 것이 아니라 서로 다른 재료로 나눠 입력해야 합니다.

![외부 렌더 이미지 · 금속성과 거칠기를 달리한 구들을 두 시점에서 비교합니다.](../Images/External/pbr-print.png)

외부 렌더 이미지 · 금속성과 거칠기를 달리한 구들을 두 시점에서 비교합니다.

읽을 곳  오른쪽 배열의 가로 방향에서 거칠기가 변할 때 작은 반사점이 넓어지는 모습을 봅니다. 세로 방향의 금속성 변화도 함께 비교합니다. UE와 광원·톤매핑이 같은 비교 자료는 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 40](https://learnopengl.com/PBR/Lighting)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 실습 절차

같은 구에 Metallic 0과 1, Roughness 0.2와 0.8의 조합을 만듭니다. 처음에는 고정 조명에서 네 구를 비교하고, 이후 재질을 유지한 채 넓은 광원의 방향만 바꿉니다.

## 예상 결과와 이유

거칠기 변화는 반사의 퍼짐을, 금속성 변화는 확산·스펙큘러 색 반응을 바꿀 것입니다. 광원을 움직이면 하이라이트도 움직여야 합니다.

## 결과를 어떻게 해석할까

기본 색에 밝은 얼룩이 고정돼 남는다면 구워 넣은 조명 흔적인지 살핍니다. 금속이 검게 보이면 Metallic부터 임의로 낮추기 전에 반사할 환경이 있는지 확인합니다.

## 실제 제작에서의 선택

금속·도장·녹을 재료로 구분한 뒤 입력을 정합니다. 외관이 어색할 때 텍스처와 조명을 동시에 고치지 않습니다.

## 이해한 뒤 확인할 조건

순수 재료의 Metallic은 0 또는 1을 기준으로 하고 경계의 필터링 등에는 중간값이 생깁니다. sRGB·데이터 채널 패킹은 입력 저장의 심화 항목으로 분리합니다.

## 공식 자료와 확장

- [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)
- [Using Fresnel](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-fresnel-in-your-unreal-engine-materials)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
