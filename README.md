# Midi2Logic

정보.txt 파일은 D드라이브 안에 다른 폴더 없이 있어야 합니다. (파일 경로가 D:\ 이어야 함)
이 파일의 인코딩 방식은 UTF-8이어야 하고, 이름은 따옴표나 다른 요소 없이 '정보'여야 합니다.

이 프로그램을 사용하려면 파이썬과 mido 모듈(현재 1.2.10)이 필요합니다. 또한, IDLE로 실행하는 것이 좋습니다.
mido 모듈을 설치하려면 명령 프롬프트에 따옴표 없이 'pip install mido'라고 입력하세요.
(아, 참고로 저는 파이썬 3 씁니다. 컴퓨터에 파이썬 2도 있는데 mido 설치하려니까 거기에 깔려서 수동으로 옮겼습니다.)

프로그램에서는 맨 위 4줄만 읽습니다. (밑에 설명을 쓸 수 있는 이유)
첫 번째 줄은 2, 4번째 줄의 파일이 이미 존재하면 경고를 띄웁니다. 이 기능은 프로그램 내에서 끌 수 있습니다.
두 번째 줄은 미디 파일을 읽어서 저장할 txt 파일의 위치(미디를 한 줄씩 읽기에 유용)이고
세 번째 줄은 midi 파일의 위치, 네 번째 줄은 미디를 로직 코드로 변환해 저장할 txt 파일의 위치입니다.
파일 경로를 입력할 때 \(역슬래시)는 /(슬래시)로 바꿔서 입력하고, 파일명과 확장자까지 입력해야 합니다.

!!! 주의: txt 파일은 쓰기를 해야 하기 때문에, 파일 경로에 같은 이름의 파일이 있다면 기존 파일이 경고 없이 삭제됩니다! !!!
(이것 때문에 예전에 만들었던 로직 코드 써놓은거 하나 날라감)

가끔씩 인코딩 에러가 나는지 자동으로 미디 파일을 읽지 못할 때가 있습니다. 그럴 때는 Squeezed text라 쓰인 부분을 복사해서
미디 파일이 저장되는 곳(이 파일의 두 번째 줄에 쓰인 곳)에 직접 붙여넣어 저장해주면 됩니다.
만약 붙여넣기를 하지 않고 강제로 진행하려 하면 파일이 비어 있기 때문에 에러가 납니다.

변환 완료 시 셸 창에 blocks와 lines가 표시되는데 blocks는 미디를 온전히 연주하는 데 필요한 노트 블록의 수이고
lines는 연주'에만' 필요한 코드 줄 수입니다. (스위치 상태 감지, 메모리 셀 입출력 등은 제외)
84개의 노트 블록이 각각 한 가지 음만 연주하는 건반 모드가 켜져 있으면 blocks는 84로 고정됩니다.

변환할 때 연주 코드가 900줄이 넘으면 900줄 초과(때에 따라 정확히 900줄이 될 수도 있지만요.)라고 경고를 띄우는데,
한 프로세서에 최대 999줄까지 들어갈 수 있기 때문에 알아서 잘 보고 복붙해주시면 됩니다.

노트 블록을 연주하는 모든 프로세서는 모든 노트 블록(block1, block2...)과 메모리 셀(cell1)에 연결되어 있어야 하며,
특히 첫 번째와 마지막 프로세서는 스위치(switch1)에도 연결되어 있어야 합니다.
메모리 셀의 0번 칸은 연주할 악기(0~9까지 가능)를 결정하며, 1번 칸은 연주할 파트(0부터 시작, 자동으로 관리됨)를 결정합니다.
