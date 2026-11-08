# CH17 Nanite와 가상화 지오메트리

## 중심 질문

Nanite는 원본의 수많은 삼각형을 매번 모두 그릴까?

## 먼저 알아둘 답

Nanite는 가시성과 화면 오차를 기준으로 필요한 삼각형 묶음과 세부 수준을 선택합니다.

## 왜 알아야 할까

고밀도 배경 에셋에 디테일을 사용할 수 있는 이유와 남아 있는 비용을 이해하기 위해 배웁니다.

### 예제 학습 목표

원본을 바꾸지 않고 화면 크기에 따라 선택되는 Nanite 세부를 관찰합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH17_Nanite/Maps/L_CH17_Nanite`

## 왜 이런 결과가 생길까

Nanite는 메시를 작은 삼각형 묶음인 클러스터와 그 계층으로 구성합니다. 가까운 부분에는 세밀한 표현을, 작게 보이는 부분에는 허용 오차 안의 거친 표현을 선택합니다. 필요한 데이터는 스트리밍으로 공급합니다. 원본 삼각형 수가 그대로 매 프레임의 표시 삼각형 수가 되지 않는 이유입니다.

## 제작 중에는 이렇게 나타납니다

모델링 예산을 원본 폴리곤 하나로만 제한하던 판단은 달라질 수 있습니다. 하지만 같은 화면을 겹쳐 덮는 표면과 재질·조명·그림자 계산까지 사라지는 것은 아닙니다.

![직접 제작 세부 선택 개념도. 원거리 결과도 비교를 위해 같은 크기로 확대했습니다. 줄인 형상과 원래 경계의 차이를 봅니다.](../Images/Focused/focus-17.png)

직접 제작 세부 선택 개념도. 원거리 결과도 비교를 위해 같은 크기로 확대했습니다. 줄인 형상과 원래 경계의 차이를 봅니다.

## 실습 절차

Nanite 바위 하나를 고정하고 카메라를 가까이에서 멀리 이동합니다. Nanite Visualization의 Triangles와 Clusters를 각각 관찰합니다. 원본 메시를 수정하지 않은 채 선택된 세부가 어떻게 달라지는지 기록합니다.

## 예상 결과와 이유

거리에 따라 선택되는 삼각형과 클러스터가 달라지면서 최종 실루엣은 가능한 범위에서 유지될 것입니다. 표시색은 재질색이 아니라 선택 단위를 구분하는 진단입니다.

## 결과를 어떻게 해석할까

원본 개수와 화면에 선택된 정보를 구분합니다. 자동 선택이 외관에 충분한지는 실제 출력 크기의 실루엣·구멍·그림자로 판단합니다.

## 실제 제작에서의 선택

고밀도 바위와 건축에서는 원본 디테일을 활용하되, 얇은 잎·겹침·변형은 별도 적합성 검증을 합니다.

## 이해한 뒤 확인할 조건

Preserve Area의 잎 면적 보존, 폴백 메시와 플랫폼 지원은 적용 대상에 따라 추가 확인합니다. 본문의 개념도는 선택 원리를 설명하며 실제 클러스터 수나 성능을 재현하지 않습니다.

## 공식 자료와 확장

- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
