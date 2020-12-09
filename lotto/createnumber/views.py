from django.shortcuts import render, HttpResponse
import random
import clipboard
from PIL import Image
import numpy as np
from tkinter import messagebox

# Create your views here.

# im = Image.open('img/18.png')  # 이미지 파일 크기 변환 코드
# print(im.size)
# im2 = im.resize((80, 80))
# im2.save('img/18.png')
# print(im2.size)


def createnumber(request):
    nb = {}
    rn = []
    if request.method == 'GET':
        nb['re'] = '?'
        return render(request, 'createnumber.html', nb)
    elif request.method == 'POST':
        if 'fdsa' in request.POST:
            nb['re'] = '?'

            return render(request, 'createnumber.html', nb)

        elif 'asdf' in request.POST:
            while len(rn) < 6:
                a = random.randint(1, 45)
                rn.append(a)
                rn = list(set(rn))
                rn.sort()

            nb['n1'] = rn[0]
            nb['n2'] = rn[1]
            nb['n3'] = rn[2]
            nb['n4'] = rn[3]
            nb['n5'] = rn[4]
            nb['n6'] = rn[5]

            clipboard.copy(str(rn[0])+','+str(rn[1])+','+str(rn[2]) +
                           ','+str(rn[3])+','+str(rn[4])+','+str(rn[5]))

            return render(request, 'createnumber.html', nb)


def dream(request):
    nb = {}
    if request.method == 'GET':
        nb['re'] = '?'
        return render(request, 'dream.html', nb)
    elif request.method == 'POST':
        if 'dr' in request.POST:
            if ['nc'] == request.POST.getlist('dr'):
                nb['message'] = '?'
                return render(request, 'dream.html', nb)
            elif ['gd'] == request.POST.getlist('dr'):
                nb['gdgd1'] = ['조상 꿈\n\n조상 관련 꿈은 꿈에서 조상이 어떤 행색이고 \n어떤 행동을 했는지가 중요합니다.\n조상이 밝고 긍정적인 모습이었다면 굉장한 길몽입니다.\n꾸짖거나 부정적 모습이었다면 \n경고가 담긴 꿈이라고 볼 수 있습니다.\n특히 알려준 내용이 생생하다면 그 내용을 \n기억하고 마음 속에 품고 지내는게 좋습니다.\n\n특히 조상님이 재물을 주는 꿈, 조상님과 식사를 하는 꿈, \n조상님이 좋은 표정으로 집으로 들어오는 꿈, \n조상님께 큰 절을 한 꿈, \n조상님이 칭찬해주는 꿈, 조상님이 번호를 알려주는 꿈은 \n매우 매우 좋으니 당장 뛰어가서 복권을 사시길~']
                nb['gdgd2'] = ['똥/쓰레기\n\n똥은 긍정적인 뜻을 많이 내포하고 있습니다. \n똥은 보통 재물을 뜻하기도 하는데 똥을 치우는 꿈보다 \n만지고 넘치고 하는 꿈들이 굉장한 길몽으로 풀이 됩니다. \n허나 똥 위에 앉는 것은 구설수에 \n오를 수 있다는 뜻이니 조심할 필요가 있겠습니다. \n반면 쓰레기는 보통 부정적인 뜻을 \n가지고 있는 경우가 많아 정리하거나 \n버리는 꿈이 매우 좋은 꿈이다.\n특히 똥 무더기에 빠져서 기분 좋게 \n허우적대는 꿈은 로또 사십시옹~']
                nb['gdgd3'] = [
                    '동물\n\n웬만한 동물이 나오는 꿈은 좋다고 보면 됩니다. \n돼지, 호랑이, 뱀, 잉어, 용, 사슴, 학, 소, \n고양이, 양, 사자 등이 있겠습니다. \n하지만 검은소나 염소 관련 꿈은 \n흉몽으로 해석 되기도 하니 조심조심..! \n길몽의 동물들은 튼튼하고 윤기가나야 더욱 좋습니다. \n특히 돼지나 황소 꿈은 행운이 가득하니 \n로또사러 고고~']
                nb['gdgd4'] = ['해/달\n\n해와 달이 나오는 꿈은 대체적으로 길몽이라 하곤 합니다. \n해와 달이 높고 빛이 강할수록 \n좋은 기운이 강한 꿈이며 날이 맑을 수록 좋다. \n구름이 끼어 잘 안보이거나 날이 흐리다면 \n좋지 않으니 조심하길..! \n특히 하늘 높이 달려 있으며 \n그곳을 향해 하늘로 올라가는 꿈은 \n당장 복권 명당으로 달리세요!']
                nb['gdgd5'] = ['하늘/날씨\n\n보통 날씨는 마음의 상태를 나타낸다고들 한다. \n꿈 속에서 하늘과 날씨가 맑으면 \n마음 상태가 좋고 컨디션이 좋아 \n현실에서 어떤 일을 하더라도 술술 풀리고 \n자신감이 넘친다는 뜻을 가진답니다. \n날씨는 마지막에 맑은 것이 중요하며 \n날씨가 흐리면 부정적인 기운을 가지지만 \n눈이나 비가 기분 좋게 내린다면 오히려 좋을 수 있다는 사실! \n특히 무지개를 본다면 행운이 깃들 것이니 \n당장 뛰쳐나가 로또사시어요~']
                nb['gdgd6'] = ['물/불\n\n보통 물과 불이 꿈에 나오면 재수가 좋고 \n금전과 재물 관련 꿈일 가능성이 높습니다. \n불은 강하고 뜨겁게 타야하며 물은 보다 맑아야 좋은 꿈입니다. \n물이 흐리거나 불이 꺼지고 있다면 \n좋지 않은 기운을 가진 꿈이니 조심하시어요. \n특히 집이 활활 타거나 정말 기분 좋은 만큼 맑은 물이 흐른다면 \n지금 당장 달려가세요! 어디로? 복권사러~']
                nb['gdgd7'] = ['피\n\n피가 꿈에 나온다면 보통 재수가 좋습니다. \n금전이 관련되지 않더라도 재수가 좋으니 \n무엇이든 도전해보는 것을 추천!! \n피가 많이면 많을수록 좋으며 \n피의 양이 적거나 피가 날 상황에 나지 않는다면 \n풀이가 좋지 않으니 조심조심..! \n자신이 흉기에 찔리거나 혹은 타인을 찔러도 \n피만 많이 본다면 재물운이 펑펑~~~ \n특히 많은 피를 마신다거나 엄청 흘려 죽는다? \n당장 나가서 복권 사세요.']
                nb['gdgd8'] = ['돈\n\n돈에 관한 꿈은 해석이 다양하며 \n좋게도 안좋게도 해몽이 된답니다. \n하지만 대부분 긍정적인 뜻이 강하며 \n재물이나 지폐가 깨끗하고 새것일수록 \n좋은 기운이 강한꿈일 가능성이 큽니다. \n꿈에서 돈은 나에게로 들어와야 좋으며 \n흩어지거나 기분이 안좋은 상태로 세고 있다면 \n그닥 좋지 못하다는 사실.. \n특히 새지폐가 가득 생기거나 나에게 쏟아지며 \n나무에 잎이 돈으로 바뀐다면? \n말해뭐해 당장나가서 사버리세요!']
                nb['gdgd9'] = [
                    '사람\n\n유명인(대통령, 유명인사) 예수님, 부처, 선인, \n죽은사람, 고귀한 사람 등을 \n꿈에서 만난다면 길몽으로 볼 수 있습니다. \n중요한건 만났을 때 기분이 좋거나 편해야합니다. \n일반적인 사람이나 지인을 만났다면 \n안색이 밝고 건강한 모습이어야 합니다. \n아기를 낳는 꿈 또한 길몽으로 보는데 \n아기의 상태가 건강할수록, 낳은 아이의 수가 많을수록 \n좋은기운이 배가 되니 알아두시길! \n특히 이런 사람들과 즐겁게 대화를 나누거나 식사를 한다면 \n복권사시는 거 강추강추!']

                return render(request, 'dream_gd.html', nb)
            elif ['bd'] == request.POST.getlist('dr'):
                nb['bdbd1'] = ['이빨/손톱\n\n이와 손톱은 안 좋은 꿈으로 풀이되는 경우가 많습니다. \n이가 빠지거나 깨지는 꿈은 \n자신감이 떨어지고 있는 사람들이 자주 꿀 수 있으며 \n손톱이 색이 변하거나 빠지는 꿈은  \n근심거리가 생기거나 나의 실수로 인해 \n타인이 피해를 볼 수 있다는 징조일 수 있습니다. \n물론 재물손실 또한 야기할 수 있기에 조심하는 것이 좋아요! \n이런 꿈을 꿨다면 자신감을 가지도록 \n더욱 당당하게 행동하고 말조심을 할 수 있도록 하자구요!']
                nb['bdbd2'] = ['벌레\n\n벌레가 나오는 꿈은 일반적으로 좋지 못합니다. \n건강상에 문제가 생길 수 있음을 암시하는 경우가 많고 \n금전적으로 좋지 못한 뜻을 내포할 수 있습니다. \n특히 썩은 음식에 구더기를 보거나 \n벌레에 물리는 꿈이라면 더욱 좋지 못하니 \n빨리 잊고 훌훌 털어버리는 것이 상책! \n하지만 반대로 집에 터질듯이 많은 벌레들이 있다면 \n오히려 좋은 뜻으로 해석될 수 있으니 \n이왕 벌레가 나왔다면 상상력을 발휘해 \n터질정도로 많이 만들어버리는 것도 나쁘지 않을지도..?']
                nb['bdbd3'] = [
                    '도망\n\n꿈에서 도망가거나 쫒기는 꿈은 \n현실에서 누군가에게 압박을 받고있거나 \n현실에 불안감이 있을 수 있다는걸 뜻하며 \n앞으로의 일이 이로인해 좋지 않을 수 있음을 암시합니다. \n더불어 떨어지거나 가라앉는 꿈도 \n정신적으로 힘든 경우가 많다고 하니 \n조금더 우리 자기 자신을 돌보는데 힘을 써보아요^^']
                nb['bdbd4'] = [
                    '동물\n\n대부분의 동물 꿈은 길몽에 속하나 \n검은 소 또는 염소 관련된 꿈은 \n좋지 않은 기운을 내포한 경우도 있습니다. \n검은소나 염소 꿈은 불길한 \n일들이 있을 수 있음을 암시합니다. \n그러니 검은소나 염소가 나왔다고 한다면 \n몸 가짐을 조심히 하고 주의하도록 합시다!']
                nb['bdbd5'] = ['싸움\n\n싸우는 꿈 같은 경우 안좋게 풀이될 때가 많은 꿈 입니다. \n누구와 싸웠는지가 중요하며 \n가족이나 지인들과는 싸우지 않는것이 좋습니다. \n웬만하면 마찰없이 지나가는 것이 좋으며 \n싸움이 있다면 말리는 것이 좋습니다. \n시비가 붙는다면 차라리 말싸움보다는 \n크게 치고 박고 싸우시는 것이 \n더 큰 불행을 피할 수 있으니 참고하세요!']
                nb['bdbd6'] = ['귀신\n\n귀신꿈은 건강과 스트레스와 관련된 것이 많습니다. \n귀신에게 쫒겨다니거나 두려워 떨고 있다면 \n건강이나 집에 우환이 생길 수 있으며 \n귀신이 또렷하게 보였다면 \n스트레스가 몰려올 수 있음을 암시합니다. \n귀신이 나와 나의 감정이 부정적이었다면 \n건강이 안좋아지거나 구설수에 오르는 등 \n억울하거나 우환 같은 것이 생길 수 있으니 \n꿈에 귀신이 보인다면 때려잡던가 \n쫒아내는 것이 좋으니 당당하게 맞서보자구요!']
                nb['bdbd7'] = ['흉터\n\n흉터가 생기거나 다치는꿈은 \n실제로 다칠수도 있는 가능성을 가지는 꿈이 많습니다. \n다치지 않더라도 난관이나 부정적인 상황들이 \n실제로 다가올 수 있으니 \n항시 몸가짐을 조심히 하는 것이 좋습니다. \n하지만 다치거나 흉터가 생길 때 \n피를 많이 본다면 오히려 좋게 해석 가능하니 \n이왕 다치는 꿈을 꾸고 있다면 \n피를 많이 볼 수 있게 합시다!']
                nb['bdbd8'] = [
                    '음식\n\n음식관련 꿈 중에는 탕에 관련된 꿈이 \n좋지 않은 기운을 담고 있는 경우가 많이 있습니다. \n꿈 속에서 탕 종류의 음식을 먹었다면 \n위장이나 장에 질환이 생길 수 있고 \n배가 아플 수 있으니 \n꿈에서 깬다면 건강 관리에 유의해보는 것이 어떨까요?']
                nb['bdbd9'] = ['나체\n\n꿈에서 나체나 어울리지 않는 옷을 입고 있는 등 \n수치스러운 꿈을 꾸었다면 \n현실에서 자신의 컴플렉스나 숨기고 싶은 비밀들이 \n알려질까봐 두려워하거나 혹은 \n그것이 현실에서 드러날지도 모른다는 것을 암시합니다. \n허나 꿈에서 나체를 부끄러워하지 않는다거나 \n이상한 옷을 입은걸 즐긴다면 \n크게 문제될것이 없다고 풀이가 된다고 합니다. \n그러니 우리 모든 순간 당당하게 굴자구요! \n그리하면 현실에서 안 될 일도 잘 풀릴지도..?']

                return render(request, 'dream_bd.html', nb)


def home(request):
    return render(request, 'home.html')
