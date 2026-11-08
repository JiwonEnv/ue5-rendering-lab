# 전체 챕터 보완 기록

26개 챕터의 용어·인과 관계·이미지의 관찰 가능성·실습의 통제 조건을 점검했습니다. 각 챕터에 관찰 절차와 오판을 피하는 기준을 추가했습니다.

CH01은 직접 제작한 장면과 실제 캡처입니다. CH02–26은 기본 레벨과 제작·검증 절차이며, 외부 이미지는 비교·학습을 위한 사례입니다. 이 보완에서 해당 레벨의 새 실측을 수행했다고 주장하지 않습니다.

| 챕터 | PDF 시작 쪽 | 추가·수정한 내용 |
|---|---:|---|
| [CH01](Chapters/CH01_RenderingPipeline.md) | 4 | 좌표·깊이 진단의 해석 범위 재점검 |
| [CH02](Chapters/CH02_ForwardDeferred.md) | 18 | 렌더러 비교의 기능·화질 동등 조건 보강 |
| [CH03](Chapters/CH03_GBuffer.md) | 20 | 진단 화면과 실제 버퍼 저장 형식 구분 |
| [CH04](Chapters/CH04_DBufferDecals.md) | 22 | 공식 데칼 전후 이미지와 수신 표면 검증 |
| [CH05](Chapters/CH05_DepthEarlyZ.md) | 24 | 깊이 검사 비교와 Early Z 이득의 차이 설명 |
| [CH06](Chapters/CH06_Overdraw.md) | 26 | 실제 Quad Overdraw 화면과 비용 오판 교정 |
| [CH07](Chapters/CH07_PBR.md) | 28 | 금속성·거칠기 비교 조건 보강 |
| [CH08](Chapters/CH08_BRDF.md) | 30 | 광원 크기와 거칠기 분리 검증 |
| [CH09](Chapters/CH09_Fresnel.md) | 32 | 물리 반사와 아트용 각도 마스크 구분 |
| [CH10](Chapters/CH10_ShadersWPO.md) | 34 | 실제 셰이더 통계 화면과 WPO·순열 검증 분리 |
| [CH11](Chapters/CH11_Substrate.md) | 36 | 공식 코팅 비교와 두 변수 동시 변경의 한계 명시 |
| [CH12](Chapters/CH12_TranslucencyRefraction.md) | 38 | 정렬·화면 기반 굴절 검증 보강 |
| [CH13](Chapters/CH13_SubsurfaceScattering.md) | 40 | 실제 산란 비교와 모델별 입력 의미 구분 |
| [CH14](Chapters/CH14_DrawCalls.md) | 42 | 공식 그리기 파이프라인과 시간·호출 수 구분 |
| [CH15](Chapters/CH15_Instancing.md) | 44 | 인스턴스별 데이터의 실제 렌더 예시 |
| [CH16](Chapters/CH16_LOD.md) | 46 | LOD 전환의 실루엣·그림자·출력 조건 보강 |
| [CH17](Chapters/CH17_Nanite.md) | 48 | 실제 Nanite 시각화의 적용 범위와 면적 보존 검증 |
| [CH18](Chapters/CH18_Culling.md) | 50 | 시야 제외·가림 판정 단계별 외부 도식 |
| [CH19](Chapters/CH19_Mipmaps.md) | 52 | 밉·필터·상주 상태를 분리한 관찰 |
| [CH20](Chapters/CH20_TextureStreaming.md) | 54 | 실제 스트리밍 통계와 예산·수요·상주량 구분 |
| [CH21](Chapters/CH21_Lumen.md) | 56 | 실제 Lumen 반사 조명 비교로 교체 |
| [CH22](Chapters/CH22_VirtualShadowMaps.md) | 58 | 실제 VSM 캐시·무효화 범위 시각화 |
| [CH23](Chapters/CH23_TAA.md) | 60 | AA 전후 확대와 정지 이미지의 한계 명시 |
| [CH24](Chapters/CH24_TSR.md) | 62 | 동일 출력에서 입력 해상도 차이와 TSR 비교 |
| [CH25](Chapters/CH25_CPUGPUBottlenecks.md) | 64 | 실제 프레임 그래프에서 계산·대기 구분 |
| [CH26](Chapters/CH26_GPUProfiling.md) | 66 | 실제 GPU Insights 시간축과 계층 시간 검증 |

## 공통 보완

- 원리·작동 과정 바로 아래에 외부 진단 화면이나 비교 이미지를 배치했습니다.
- 다음 쪽에 아트 실무·비용·실습·관찰과 판단·오판 방지·요약을 묶었습니다.
- 단순 화살표나 반복 삼각형이 실제 차이를 대신하지 않도록 중복 그림을 정리했습니다.
- 과거 버전의 UI·모델·수치와 현재 프로젝트의 검증을 구분했습니다.
- 정지 이미지로 입증할 수 없는 이동 품질·캐시·시간 변화에는 별도 검증 절차를 명시했습니다.

[이미지 출처와 편집 기록](Images/Sources.md)
