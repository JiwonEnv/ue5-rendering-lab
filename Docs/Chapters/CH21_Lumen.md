# CH21 Lumen과 간접광

## 중심 질문

직접 빛이 닿지 않는 흰 벽은 왜 주변 벽의 색을 띨까?

## 먼저 알아둘 답

빛은 첫 표면에서 끝나지 않고 다른 표면으로 전달되며, Lumen은 이 간접광을 실시간으로 근사합니다.

## 왜 알아야 할까

실내의 밝기·색 번짐을 재질색과 구분하고, 라이트를 추가하기 전에 빛 전달을 진단하기 위해 배웁니다.

### 예제 학습 목표

색 벽만 바꿔 흰 벽의 재질색과 간접광을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part04_LightingAndImageQuality/CH21_Lumen/Maps/L_CH21_Lumen`

## 왜 이런 결과가 생길까

광원에서 바로 도달한 빛은 직접광입니다. 붉은 벽에 닿은 빛 일부가 다시 방 안으로 퍼져 흰 벽에 도달하면 붉은 간접광이 생깁니다. Lumen은 화면 정보와 별도 장면 표현을 이용해 이런 빛의 전달을 추정합니다. 화면에 보이는 정보만 쓰면 화면 밖 물체를 놓칠 수 있으므로 보완할 장면 정보가 필요합니다.

## 제작 중에는 이렇게 나타납니다

흰 벽이 붉게 보인다고 Base Color를 푸르게 보정하면 다른 조명에서 재질이 틀어질 수 있습니다. 먼저 표면의 고유 색과 들어오는 간접광을 구분해야 합니다.

![간접광의 색 전달](../Images/Concepts/cornellbox.png)

외부 경로 추적 Cornell box 렌더. 색 벽의 간접광 현상을 설명하며 Lumen 실행 결과는 아닙니다. 원본 전체·색상·비율 유지.

[Trevorgoodchild · Public domain · 출처 36](https://commons.wikimedia.org/wiki/File:Cornellbox_pathtracing_irradiancecaching.png)

## 실습 절차

한쪽 벽만 색이 있는 작은 방과 흰 수신 벽을 준비합니다. Lumen GI와 노출·직접광을 고정합니다. 색 벽의 Base Color만 빨강에서 중성 회색으로 바꾸고 수신 벽의 Base Color와 Lit를 비교합니다.

## 예상 결과와 이유

수신 벽의 Base Color는 유지되고 Lit의 색 번짐은 달라질 것입니다. 직접광은 같아도 주변 재료가 간접 조명을 바꾼다는 예상입니다.

## 결과를 어떻게 해석할까

변화가 없으면 GI 설정과 장면 표현을 먼저 확인합니다. Surface Cache는 추적한 표면의 재질·조명을 조회하는 저장 체계입니다. 누락을 조사할 때 진단하지만 이 장의 첫 결론은 색 번짐의 원인입니다.

## 실제 제작에서의 선택

수신 벽의 텍스처를 바로 보정하지 말고 주변 표면·간접광·노출을 조사합니다. 표현 누락은 Lumen Scene과 Surface Cache를 다음 진단 대상으로 삼습니다.

## 이해한 뒤 확인할 조건

반사에서 Surface Cache와 Hit Lighting을 비교하는 것은 별도 문제입니다. 반사 모드나 추적 옵션을 이 간접광 실험과 동시에 바꾸지 않습니다.

## 공식 자료와 확장

- [Lumen Technical Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine)
- [Lumen Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
