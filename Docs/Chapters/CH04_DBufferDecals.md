# CH04 DBuffer와 데칼

## 중심 질문

데칼은 왜 벽 그림처럼 빛에 반응하고, 옆 소품에도 묻을까?

## 먼저 알아둘 답

DBuffer 데칼은 투영 범위 안의 표면 정보를 바꾸고, 바뀐 표면이 이후 조명 계산에 참여합니다.

## 왜 알아야 할까

반복 벽에 얼룩과 손상을 더하면서 투영 오류와 불필요한 처리 범위를 제어하기 위해 배웁니다.

### 예제 학습 목표

벽의 얼룩을 유지하면서 박스 깊이만 줄여 잘못 묻는 소품을 제외합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH04_DBufferDecals/Maps/L_CH04_DBufferDecals`

## 왜 이런 결과가 생길까

데칼 Actor의 박스는 그림을 적용할 3D 범위를 정합니다. 엔진은 깊이 정보로 수신 표면의 위치를 찾고, 박스 안에 해당하는 데칼 값을 준비합니다. DBuffer는 그 색·거칠기·법선 변경을 잠시 담는 버퍼입니다. 벽의 Base Pass가 이를 읽어 표면에 반영하므로 단순히 화면 위에 붙인 스티커와 다르게 조명에 반응합니다.

## 제작 중에는 이렇게 나타납니다

박스는 원하는 벽 이름만 골라 투영하는 것이 아닙니다. 깊이가 과하면 그 안에 들어간 소품도 수신 조건에 따라 영향을 받습니다. 보이는 얼룩 크기와 투영 공간의 크기를 구분해야 합니다.

![공식 비교 이미지 · 같은 돌벽에 데칼을 적용하기 전과 후입니다. UE 5.5 문서의 사례입니다.](../Images/External/decal-print.png)

공식 비교 이미지 · 같은 돌벽에 데칼을 적용하기 전과 후입니다. UE 5.5 문서의 사례입니다.

읽을 곳  반복되는 벽돌 위에 생긴 손상과 표면 변화가 어디까지 이어지는지 봅니다. 데칼 수나 성능의 통제 실험은 아니므로 투영 면적·겹침의 비용은 실습에서 따로 측정합니다.

[© Epic Games · 공식 문서 · 출처 46](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine?application_version=5.5)

원본 전체 유지 · 투명 배경은 흰색으로 표시

원저작권과 원문 출처 표시는 유지합니다

## 실습 절차

벽 앞에 작은 소품을 놓고 하나의 얼룩 데칼을 투영합니다. 먼저 큰 박스에서 잘못 묻는 표면을 찾고, 데칼의 전면 크기는 유지한 채 박스 깊이만 줄입니다.

## 예상 결과와 이유

벽의 얼룩은 남고 박스 밖으로 빠진 소품의 얼룩은 사라질 것입니다. 이후 라이트 방향만 바꾸면 얼룩을 포함한 표면이 빛에 함께 반응할 것입니다.

## 결과를 어떻게 해석할까

소품에 계속 묻으면 실제 박스 위치와 수신 설정을 확인합니다. 색만 비교하지 말고 거칠기나 법선 변경도 확인해야 물기·스크래치 데칼의 효과를 놓치지 않습니다.

## 실제 제작에서의 선택

원하는 표면을 충분히 덮는 최소한의 투영 범위를 사용합니다. 넓은 중첩은 화면에서 같은 영역을 반복 처리할 수 있으므로 큰 박스를 관성적으로 유지하지 않습니다.

## 이해한 뒤 확인할 조건

Receives Decals는 물체의 수신 여부, Decal Response는 재질이 받을 변경을 정합니다. 다른 데칼 경로와 적용 순서는 공식 자료의 심화 항목입니다.

## 공식 자료와 확장

- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
