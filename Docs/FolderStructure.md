# 폴더와 에셋 규칙

```text
ue5-rendering-lab/
├── RenderingLab.uproject
├── Config/                         프로젝트 설정
├── Content/
│   ├── Python/                     에디터 생성·검증 도구
│   └── RenderingLab/
│       ├── Maps/                   시작 레벨
│       ├── Common/                 여러 챕터가 공유하는 에셋
│       │   ├── Materials/
│       │   ├── Meshes/
│       │   ├── Textures/
│       │   └── Blueprints/
│       └── Chapters/
│           ├── Part01_RenderingBasics/
│           ├── Part02_MaterialsAndLight/
│           ├── Part03_GeometryAndTextures/
│           ├── Part04_LightingAndImageQuality/
│           └── Part05_Profiling/
│               └── CH26_GPUProfiling/
│                   ├── Maps/
│                   ├── Materials/
│                   ├── Meshes/
│                   ├── Textures/
│                   └── Blueprints/
├── Docs/
│   ├── chapters.json               챕터 ID와 학습 순서의 기준
│   ├── Chapters/                   챕터별 실습 설명과 제작 기록
│   ├── Guide/                      학습 문서 원본
│   └── Images/                     문서에 사용하는 캡처
├── Scripts/                        실행 도구
├── .gitattributes                  바이너리 에셋의 LFS 설정
└── CONTRIBUTING.md                 커밋 규칙
```

모든 챕터는 Maps, Materials, Meshes, Textures, Blueprints 하위 폴더를 가집니다.
빈 폴더는 `.gitkeep`으로 보존합니다. 에디터에서 빈 폴더가 안 보이면 Content Browser의
Show Empty Folders 설정을 확인합니다.

레벨은 `L_`, 머티리얼은 `M_`, 인스턴스는 `MI_`, 메시 에셋은 `SM_`,
텍스처는 `T_`, 블루프린트는 `BP_`를 접두사로 사용합니다.
챕터 전용 에셋 이름에는 `CH07`과 같은 ID를 포함합니다.
공용 에셋은 Common만 참조하고, 챕터 사이에는 직접 참조를 만들지 않습니다.
에셋 이동은 언리얼 에디터에서 하고 redirector 정리 후 영향을 확인합니다.

Forward/Deferred, Substrate 형식 등은 프로젝트 범위 설정입니다.
서로 다른 맵만 열어 설정이 자동으로 전환된다고 가정하지 않습니다.
CH02 문서의 절차에 따라 변경하고 재시작이 필요한 경우 재시작합니다.
