# UE5 Rendering Lab

게임 배경 아티스트를 위한 언리얼 엔진 5 렌더링 원리와 최적화 실습 프로젝트입니다.

## 현재 구성

UE 5.8.4의 콘텐츠 전용 프로젝트입니다. 시작 레벨과 챕터별 기본 실습 레벨을 제공합니다.
CH01은 쇼윈도 골목과 12개의 실제 진단·A/B 캡처를 제공합니다.
나머지 기본 레벨에는 공통 비교 무대, 조명, 고정 노출, 카메라와 비교용 구가 있습니다.
챕터별 특화 기능을 구현하는 절차는 각 실습 문서에 정리되어 있습니다.
`기본 레벨 준비` 상태의 챕터는 해당 기능의 완성 예제가 될 때까지 추가 제작이 필요합니다.

## 시작하기

1. UE 5.8.4와 Git LFS를 준비합니다.
2. 저장소를 복제한 뒤 `git lfs pull`로 바이너리 에셋을 받습니다.
3. `RenderingLab.uproject`를 엽니다. 첫 실행은 셰이더와 거리장 준비에 시간이 걸릴 수 있습니다.
4. 시작 레벨 `Content/RenderingLab/Maps/L_RenderingLab`을 확인합니다.
5. 아래 실습 문서에서 레벨 경로를 확인하고 해당 챕터 맵을 엽니다.

에디터 시점을 비교 구도로 맞추려면 Outliner에서 `ComparisonCamera`를 선택하고
카메라를 Pilot합니다. Play에서도 자동 활성화 카메라로 비교 무대를 볼 수 있습니다.

Windows DX12 SM6, Deferred, Lumen, Virtual Shadow Maps, TSR,
Substrate Blendable을 시작 설정으로 사용합니다. 대상 기기에서 기능 지원을 확인하세요.
Forward 전환이나 Adaptive GBuffer 실험은 프로젝트 설정 변경과 재시작이 필요할 수 있습니다.

## 학습 순서

<!-- Generated from Docs/chapters.json by Scripts/manage_chapters.py -->
| ID | 주제와 실습 절차 | 제작 상태 |
| --- | --- | --- |
| CH01 | [렌더링 파이프라인](Docs/Chapters/CH01_RenderingPipeline.md) | 실습 검증 완료 |
| CH02 | [Forward와 Deferred](Docs/Chapters/CH02_ForwardDeferred.md) | 기본 레벨 준비 |
| CH03 | [GBuffer와 표면 정보](Docs/Chapters/CH03_GBuffer.md) | 기본 레벨 준비 |
| CH04 | [DBuffer와 데칼](Docs/Chapters/CH04_DBufferDecals.md) | 기본 레벨 준비 |
| CH05 | [Depth와 Early Z](Docs/Chapters/CH05_DepthEarlyZ.md) | 기본 레벨 준비 |
| CH06 | [Overdraw와 화면 겹침](Docs/Chapters/CH06_Overdraw.md) | 기본 레벨 준비 |
| CH07 | [PBR과 재질 입력](Docs/Chapters/CH07_PBR.md) | 기본 레벨 준비 |
| CH08 | [BRDF와 반사 분포](Docs/Chapters/CH08_BRDF.md) | 기본 레벨 준비 |
| CH09 | [Fresnel과 시선 각도](Docs/Chapters/CH09_Fresnel.md) | 기본 레벨 준비 |
| CH10 | [셰이더와 머티리얼](Docs/Chapters/CH10_ShadersWPO.md) | 기본 레벨 준비 |
| CH11 | [Substrate와 물질 구성](Docs/Chapters/CH11_Substrate.md) | 기본 레벨 준비 |
| CH12 | [Translucency와 합성](Docs/Chapters/CH12_TranslucencyRefraction.md) | 기본 레벨 준비 |
| CH13 | [SSS와 표면 아래 산란](Docs/Chapters/CH13_SubsurfaceScattering.md) | 기본 레벨 준비 |
| CH14 | [Draw Call과 제출 작업](Docs/Chapters/CH14_DrawCalls.md) | 기본 레벨 준비 |
| CH15 | [Instancing과 반복 배치](Docs/Chapters/CH15_Instancing.md) | 기본 레벨 준비 |
| CH16 | [LOD와 화면 크기](Docs/Chapters/CH16_LOD.md) | 기본 레벨 준비 |
| CH17 | [Nanite와 가상화 지오메트리](Docs/Chapters/CH17_Nanite.md) | 기본 레벨 준비 |
| CH18 | [Culling과 가시성](Docs/Chapters/CH18_Culling.md) | 기본 레벨 준비 |
| CH19 | [Mipmap과 텍스처 샘플링](Docs/Chapters/CH19_Mipmaps.md) | 기본 레벨 준비 |
| CH20 | [Texture Streaming](Docs/Chapters/CH20_TextureStreaming.md) | 기본 레벨 준비 |
| CH21 | [Lumen과 간접광](Docs/Chapters/CH21_Lumen.md) | 기본 레벨 준비 |
| CH22 | [Virtual Shadow Maps](Docs/Chapters/CH22_VirtualShadowMaps.md) | 기본 레벨 준비 |
| CH23 | [TAA와 프레임 히스토리](Docs/Chapters/CH23_TAA.md) | 기본 레벨 준비 |
| CH24 | [TSR과 시간적 재구성](Docs/Chapters/CH24_TSR.md) | 기본 레벨 준비 |
| CH25 | [CPU와 GPU 병목](Docs/Chapters/CH25_CPUGPUBottlenecks.md) | 기본 레벨 준비 |
| CH26 | [GPU Profiler와 개선 검증](Docs/Chapters/CH26_GPUProfiling.md) | 기본 레벨 준비 |

## 구조와 확장

- [처음 읽는 방법](Docs/ReadingGuide.md)
- [용어집](Docs/Glossary.md)
- [보충 주석](Docs/SupplementaryNotes.md)
- [전체 챕터 보완 기록](Docs/ChapterReview.md)
- [이미지 출처](Docs/Images/Sources.md)
- [폴더 구조와 에셋 규칙](Docs/FolderStructure.md)
- [새 챕터 추가 방법](Docs/AddingChapters.md)
- [커밋 규칙](CONTRIBUTING.md)
- [한국어 학습 가이드 PDF](Docs/Guide/UE5_Rendering_Guide_KO.pdf)

챕터 ID와 에셋 경로는 유지하고 `Docs/chapters.json` 배열에서 학습 순서를 관리합니다.
새 챕터는 새 ID를 부여한 뒤 원하는 학습 순서에 배치할 수 있습니다.
공유 에셋은 `Content/RenderingLab/Common`에서 관리합니다.

## 기본 레벨 생성

에디터를 닫은 뒤 PowerShell에서 실행합니다.

```powershell
.\Scripts\BuildLab.ps1
```

생성 도구는 누락된 레벨과 공용 머티리얼을 만듭니다. 기존 에셋은 보존합니다.
검수 로그는 `Saved/Logs/LabBuild.log`에 생성되며 Git에 포함하지 않습니다.
생성 단계의 NullRHI 실행은 에셋 저장과 로드 검증용입니다.
렌더링 품질과 성능은 실제 GPU로 에디터 또는 빌드를 실행해 별도로 측정합니다.

## 자료 출처

기본 무대는 Unreal Engine에 포함된 BasicShapes를 참조하며 외부 에셋을 포함하지 않습니다.
프로젝트를 열려면 Epic Games의 Unreal Engine 설치가 필요합니다.
각 주제의 참고 링크는 학습 가이드의 출처 목록에서 확인할 수 있습니다.
