print("미디->로직 변환 프로그램 Midi2Logic")
print("설명을 전부 읽으셨길 바랍니다.")
print()

while True:
    name=input("사용자명을 입력하세요. 대소문자를 구분합니다. ")
    try:
        with open("C:/Users/"+name+"/Downloads/Midi2Logic-Downloads-/정보.txt","r",encoding="UTF-8") as file:
            file.read()
    except:
        print("파일이 존재하지 않거나 잘못된 사용자명입니다.")
    else:
        break
    finally:
        print()

import mido
with open("C:/Users/"+name+"/Downloads/Midi2Logic-Downloads-/정보.txt","r",encoding="UTF-8") as file:
    warning=file.readline().strip()
    textlocate=file.readline().strip()
    midilocate=file.readline().strip()
    logiclocate=file.readline().strip()
    left=file.read()

if warning=="on" :
    while True:
        try:
            with open(textlocate,"r") as file:
                temp=file.read()
        except FileNotFoundError:
            textnotexist=1
        else:
            textnotexist=0
        try:
            with open(logiclocate,"r") as file:
                temp=file.read()
        except FileNotFoundError:
            logicnotexist=1
        else:
            logicnotexist=0
        if textnotexist==0 or logicnotexist==0 :
            print("다음 파일이 이미 존재합니다:")
            if textnotexist==0 :
                print(textlocate)
            if logicnotexist==0 :
                print(logiclocate)
            print("계속하면 기존 파일이 삭제됩니다. 계속할까요?")
            contin=input("1은 '예', 2는 '예, 다시 표시하지 않습니다.', 그 외는 '아니요' ")
            if contin=="1" :
                print()
                break
            if contin=="2" :
                with open("C:/Users/"+name+"/Downloads/Midi2Logic-Downloads-/정보.txt","w",encoding="UTF-8") as file:
                    file.write("off\n")
                    file.write(textlocate+"\n")
                    file.write(midilocate+"\n")
                    file.write(logiclocate+"\n")
                    file.write(left)
                    print()
                    break
            print()
        else :
            print()
            break

with open(textlocate,"w") as file:
    mid=mido.MidiFile(midilocate,clip=True)
    try:
        file.write(str(mid))
    except:
        print("이런, 뭔가가 잘못되었네요. 직접 복사해 주시겠어요?")
        print("잠시만요...")
        print(mid)
        print("파일 경로: "+textlocate)
        input("저장 후 엔터를 눌러 계속합니다.")
        print()

block=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]
note=['0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.10', '0.11', '1.00', '1.01', '1.02', '1.03', '1.04', '1.05', '1.06', '1.07', '1.08', '1.09', '1.10', '1.11', '2.00', '2.01', '2.02', '2.03', '2.04', '2.05', '2.06', '2.07', '2.08', '2.09', '2.10', '2.11', '3.00', '3.01', '3.02', '3.03', '3.04', '3.05', '3.06', '3.07', '3.08', '3.09', '3.10', '3.11', '4.00', '4.01', '4.02', '4.03', '4.04', '4.05', '4.06', '4.07', '4.08', '4.09', '4.10', '4.11', '5.00', '5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '5.09', '5.10', '5.11', '6.00', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '6.07', '6.08', '6.09', '6.10', '6.11']
midi=[[1]]
track=0
temp=0
num=1
play=0
print("조정할 키를 입력하세요. 잘못된 입력은 0으로 처리됩니다. 너무 크거나 작을 경우 소리가 나지 않습니다.")
key=input("예시: D를 D#으로 바꾸고 싶으면 0.5, C#으로 바꾸고 싶으면 -0.5 ")
try:
    key=float(key)
except:
    key=-24
else:
    if key*2!=int(key*2) :
        key=-24
    else:
        key=int(key*2)-24
print()

print("배속을 입력하세요. 잘못된 입력은 1로 처리됩니다.")
speed=input("배속은 속도만 변화시키며, 음높이에는 영향을 주지 않습니다. ")
try:
    speed=float(speed)
except:
    speed=1
else:
    if speed<=0 :
        speed=1
print()

print("건반 모드를 켜시겠습니까?")
many=input("1은 '예', 그 외는 '아니요' ")
print()

with open(textlocate,"r") as file:
    with open(logiclocate,"w") as logic:
        while True:
            temp2=-1
            velo=""
            x=file.readline().strip()
            if x=="])" :
                break
            else :
                y=x.split("(")
                if y[0]=="MidiTrack" :
                    if midi[track]!=[1] :
                        track+=1
                        midi.append([1])
                    if play==1 :
                        num+=1
                        play=0
                    if tp!=1 :
                        num=1
                    temp=0
                else :
                    z=y[1].split(",")
                    for I in range(len(z)):
                        z[I]=z[I].strip()
                    if y[0]=="MidiFile" :
                        for I in range(len(z)):
                            w=z[I].split("=")
                            if w[0]=="type" :
                                tp=int(w[1])
                            if w[0]=="ticks_per_beat" :
                                tpb=int(w[1])
                    if y[0]=="MetaMessage" :
                        for I in range(len(z)):
                            w=z[I].split("=")
                            if z[0]=="'set_tempo'" :
                                if w[0]=="tempo" :
                                    temp2=int(w[1])
                            else :
                                temp2=-1
                    if y[0]=="Message" :
                        for I in range(len(z)):
                            w=z[I].split("=")
                            if z[0]=="'note_on'" :
                                if w[0]=="note" :
                                    try:
                                        temp2="control config block"+str(num)+" "+str(note[int(w[1])+key])
                                        bn=str(block[int(w[1])+key])
                                    except:
                                        temp2=-1
                                    else:
                                        if many=="1" :
                                            temp2="control config block"+bn+" "+str(note[int(w[1])+key])
                                        if int(w[1])+key<0 :
                                            temp2=-1
                                if w[0]=="velocity" :
                                    if w[1]=="0" :
                                        temp2=-1
                                    if type(temp2)!=int :
                                        velo="control color block"+bn+" inst "+str(int(bn)-1)+" "+str(int(w[1])/50)
                                if temp2!=-1 :
                                    play=1
                            else :
                                temp2=-1
                    for I in range(len(z)):
                        w=z[I].split("=")
                        if w[0]=="time" :
                            v=w[1].split(")")
                            temp+=int(v[0])
            temp2=[temp2, temp]
            velo=[velo, temp]
            if temp2[0]!=-1 :
                if many=="1" and velo[0]!="" :
                    midi[track].append(velo)
                midi[track].append(temp2)
        if midi[len(midi)-1]==[1] :
            temp2=[]
            for I in range(len(midi)-1):
                temp2.append(midi[I])
            midi=temp2

        line=0
        tline=0
        tempo=0
        total=0
        over=0
        logic.write("read inst cell1 0\n")
        logic.write("read start cell1 1\n")
        logic.write("jump 4 equal start 0\n")
        logic.write("end\n")
        if many=="1" :
            num=0
        else :
            for I in range(1,num+1):
                logic.write("control color block")
                logic.write(str(I))
                logic.write(" inst 0 0 0\n")
        logic.write("sensor on switch1 @enabled\n")
        logic.write("jump ")
        logic.write(str(7+num))
        logic.write(" equal on 1\n")
        logic.write("end\n")
        if tp==1 :
            while True:
                end=0
                for I in range(len(midi)):
                    if midi[I][0]==len(midi[I]) :
                        end+=1
                    else :
                        if I==end :
                            time=midi[I][midi[I][0]][1]
                            temp=midi[I][midi[I][0]][0]
                            temp2=I
                        else :
                            if time>midi[I][midi[I][0]][1] :
                                time=midi[I][midi[I][0]][1]
                                temp=midi[I][midi[I][0]][0]
                                temp2=I
                if end==len(midi) :
                    break
                if line>=900 :
                    over+=1
                    logic.write("write inst cell1 0\n")
                    logic.write("write ")
                    logic.write(str(over))
                    logic.write(" cell1 1\n")
                    logic.write("\n\n\n")
                    logic.write("-"*57)
                    logic.write("\n")
                    logic.write("!"*20)
                    logic.write(" 주의: 900라인 초과! ")
                    logic.write("!"*20)
                    logic.write("\n")
                    logic.write("-"*57)
                    logic.write("\n\n\n\n")
                    logic.write("read inst cell1 0\n")
                    logic.write("read start cell1 1\n")
                    logic.write("jump 4 equal start ")
                    logic.write(str(over))
                    logic.write("\n")
                    logic.write("end\n")
                    line=0
                if time-total>0 :
                    logic.write("wait "+str(((time-total)*tempo)/(tpb*1000000))+"\n")
                    total=time
                    line+=1
                    tline+=1
                if type(temp)==int :
                    tempo=temp/speed
                else :
                    logic.write(temp+"\n")
                    line+=1
                    tline+=1
                midi[temp2][0]+=1
        else :
            for I in range(len(midi)):
                time=0
                total=0
                for J in range(1, len(midi[I])):
                    temp=midi[I][J][0]
                    time=midi[I][J][1]
                    if line>=900 :
                        over+=1
                        logic.write("write inst cell1 0\n")
                        logic.write("write ")
                        logic.write(str(over))
                        logic.write(" cell1 1\n")
                        logic.write("\n\n\n")
                        logic.write("-"*57)
                        logic.write("\n")
                        logic.write("!"*20)
                        logic.write(" 주의: 900라인 초과! ")
                        logic.write("!"*20)
                        logic.write("\n")
                        logic.write("-"*57)
                        logic.write("\n\n\n\n")
                        logic.write("read inst cell1 0\n")
                        logic.write("read start cell1 1\n")
                        logic.write("jump 4 equal start ")
                        logic.write(str(over))
                        logic.write("\n")
                        logic.write("end\n")
                        line=0
                    if time-total>0 :
                        logic.write("wait "+str(((time-total)*tempo)/(tpb*1000000))+"\n")
                        total=time
                        line+=1
                        tline+=1
                    if type(temp)==int :
                        tempo=temp/speed
                    else :
                        logic.write(temp+"\n")
                        line+=1
                        tline+=1
        logic.write("set time1 @time\n")
        if many!="1" :
            for I in range(1,num+1):
                logic.write("control color block")
                logic.write(str(I))
                logic.write(" inst 0 0 0\n")
        logic.write("control enabled switch1 0 0 0 0\n")
        logic.write("set time2 @time\n")
        logic.write("op sub time time2 time1\n")
        logic.write("jump ")
        logic.write(str(line+5))
        logic.write(" lessThan time 1000\n")
        logic.write("write 0 cell1 1\n")

print("sucess!\n(",end="")
if many=="1" :
    num=84
print(num,"block",end="")
if num>=2 :
    print("s",end="")
print(",",tline,"line",end="")
if tline>=2 :
    print("s",end="")
print(")")
