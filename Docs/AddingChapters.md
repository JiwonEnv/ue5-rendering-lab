# 새 챕터 추가하기

챕터의 고유 ID와 에셋 경로를 유지하고 학습 순서는 별도로 관리합니다.
새 주제를 중간에 넣더라도 기존 챕터 번호를 변경할 필요가 없습니다.

## 추가 명령

언리얼 에디터를 닫고 프로젝트 폴더에서 PowerShell을 엽니다.

```powershell
.\Scripts\AddChapter.ps1 -Slug 'VolumetricFog' -Title '볼류메트릭 포그'
```

현재 목록의 가장 큰 ID 다음 번호를 사용해 폴더와 실습 문서를 만들고,
기본 레벨을 생성하며 README의 학습 순서 표를 갱신합니다.
26개 챕터 상태에서 실행하면 `CH27_VolumetricFog`가 추가됩니다.

중간 학습 순서에 넣고 기존 파트에 소속시키려면 다음과 같이 실행합니다.

```powershell
.\Scripts\AddChapter.ps1 -Slug 'VolumetricFog' -Title '볼류메트릭 포그' -Part 'Part04_LightingAndImageQuality' -After 'CH22'
```

새 ID는 CH27이지만 학습 목록에서는 CH22 다음에 표시됩니다.
`-After`를 생략하면 마지막에 추가하며 `-Part` 기본값은 `Part06_Extensions`입니다.
커스텀 엔진 경로는 `-EngineRoot 'D:\Epic Games\UE_5.8'`로 지정합니다.

## 기존 챕터 보존

`BuildLab.ps1`은 존재하는 맵과 공용 머티리얼을 보존하고 누락된 에셋을 생성합니다.
생성이 도중에 실패하면 원인을 수정한 뒤 `BuildLab.ps1`을 다시 실행합니다.
이미 목록에 추가한 챕터에 `AddChapter.ps1`을 다시 실행하면 중복을 거절합니다.
실습 씬을 수정한 뒤에는 저장하고 에디터를 닫은 상태에서 생성 도구를 실행합니다.

## 순서와 상태 변경

`Docs/chapters.json` 배열 안에서 항목의 순서를 바꾸고 다음 명령을 실행합니다.

```powershell
& 'C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\ThirdParty\Python3\Win64\python.exe' .\Scripts\manage_chapters.py
```

ID, slug, folder, map, notes는 에셋 경로와 연결됩니다. 순서 변경 시 그대로 유지합니다.
`title`로 표시 이름을 바꾸고 `status`는 다음 기준으로 관리합니다.

| status | 의미 |
| --- | --- |
| starter | 공용 비교 무대를 갖춘 기본 레벨 |
| implemented | 주제별 기능과 에셋 구현 |
| verified | 실습 재현과 결과 검증 완료 |

새 예제를 만든 뒤 문서에 제작 과정, 검증한 환경, 이미지와 결과를 기록합니다.
커밋 예시는 `feat(ch27): 볼류메트릭 포그 비교 씬 추가`입니다.

렌더링과 독립적인 게임플레이 시스템은 별도 레포지토리와 프로젝트로 구성할 수 있습니다.

## 문서의 설명 순서

먼저 주제의 정의와 전체 렌더링에서 맡는 역할, 입력·출력과 작동 과정을 작성합니다.
그다음 왜 제작에 필요한지와 비용을 설명하고, 확인할 예제를 하위 과제로 둡니다.
문제를 재현하는 예제 하나만으로 개념 전체를 설명했다고 보지 않습니다.
