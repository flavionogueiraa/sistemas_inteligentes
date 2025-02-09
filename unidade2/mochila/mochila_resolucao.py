import random

itens = [
    # preço, peso, volume
    [0.28456068378572996, 0.7538033676117031, 0.08245826068985862],
    [0.2335160652259063, 0.1690863407978872, 0.5731558419014972],
    [0.4445116445472611, 0.5502082058912725, 0.8631817108009812],
    [0.28318346563326036, 0.1505776279995693, 0.3898492413661614],
    [0.6714735129954122, 0.17020900749956192, 0.7622927228723103],
    [0.7991786876745178, 0.623511391378111, 0.7752025437619636],
    [0.016280085743557438, 0.3407324959998601, 0.17941218278554638],
    [0.407968328252414, 0.11306471274982088, 0.37965478259701146],
    [0.80232148053943, 0.309560625477893, 0.18352757839476674],
    [0.9124437959467011, 0.805208764023107, 0.039059849728690144],
    [0.8860645879932918, 0.18676413843445672, 0.05661208773125215],
    [0.24754810572794927, 0.7114193796289632, 0.7167125012242072],
    [0.9850541955855372, 0.0903064958683043, 0.16610378070756748],
    [0.03996123444708033, 0.6764897755742855, 0.9877176645650281],
    [0.42155419682892326, 0.2922582352186772, 0.6243992716977628],
    [0.3155920826220592, 0.4451093648216896, 0.5574235633801836],
    [0.9712335678833801, 0.9091257399097858, 0.6862441711192044],
    [0.44767182761923785, 0.34916833546199355, 0.9452194195550743],
    [0.9076399819179859, 0.829847986028833, 0.7375885589676369],
    [0.34848230011348946, 0.08822699976644144, 0.11833527168399649],
    [0.25538062057762945, 0.32292728658063685, 0.2615579752621886],
    [0.2332446952822388, 0.552847037107538, 0.9246127786680846],
    [0.7415029605970043, 0.5521400902403972, 0.3284883887822596],
    [0.8643244785838996, 0.12904297393443176, 0.36909296701550487],
    [0.4329488709290431, 0.3692482105624677, 0.893121249765379],
    [0.4383924616835829, 0.060735064012740536, 0.26167873187086943],
    [0.5939680914147861, 0.060621578844919255, 0.20149152541546433],
    [0.19038246075167609, 0.44328540542568284, 0.6563922963170075],
    [0.6634760411448103, 0.4058012056005881, 0.5518825553604633],
    [0.6403188761383342, 0.29622480923258765, 0.8429469489518984],
    [0.47373019814367, 0.4918818320867707, 0.8318767328471238],
    [0.15271624353654834, 0.26410781972218167, 0.35261031421699085],
    [0.7943637109585108, 0.7349999256643024, 0.4034059176022663],
    [0.8746180248453003, 0.9502712230799073, 0.6079429506006354],
    [0.6653562291794538, 0.6691278756674552, 0.052665797648845936],
    [0.13872240476953956, 0.5510589059262289, 0.900170855387067],
    [0.16604285139761255, 0.09718542080069392, 0.013882639161748367],
    [0.662448949007137, 0.920128858116733, 0.8123764039686485],
    [0.6388608566099443, 0.34545204603292734, 0.4048775615651389],
    [0.972236740362951, 0.30211290358555287, 0.12477160136418686],
    [0.033249615076831995, 0.9398238830602488, 0.3108660064120321],
    [0.05476831764395096, 0.042777063366493784, 0.8667762542003867],
    [0.6695775113597532, 0.9572305672721105, 0.002924107979188184],
    [0.5812622663624742, 0.02940602506203749, 0.9942154516645112],
    [0.32027064780492764, 0.8593093268989901, 0.31755790771046877],
    [0.029848191857928197, 0.06220663865883369, 0.2099782464160448],
    [0.5613968890419431, 0.8202590715291993, 0.47316730136349283],
    [0.7819025908403178, 0.9876213496230818, 0.14005356364701116],
    [0.7570019841663999, 0.3564763885227922, 0.019348111430126935],
    [0.558822619234595, 0.21092121874594283, 0.5667805330071582],
    [0.9136523743733853, 0.4690895292345776, 0.6401464562078224],
    [0.48860852136754074, 0.3081358630012321, 0.27513104221676665],
    [0.7440572402523945, 0.9243011267836262, 0.1236496572098994],
    [0.4457309047062137, 0.7780097657122278, 0.5958304964800506],
    [0.6365759080801303, 0.041417734039690624, 0.2556677897382964],
    [0.7680937349213379, 0.27182264619448104, 0.5884889649283944],
    [0.33003651273110546, 0.40829890569694205, 0.42378592696650486],
    [0.5170095397466418, 0.6331513287509408, 0.5380354297635532],
    [0.8175500054776881, 0.20514861895644332, 0.3161484377542806],
    [0.7284514872601151, 0.8662231218826411, 0.014761665298370197],
    [0.1296081362953153, 0.6562949992693521, 0.041125440070632124],
    [0.8158421282021736, 0.5817191475621599, 0.5345977016463251],
    [0.9499341510906121, 0.3746928541404616, 0.7163720293085677],
    [0.10785402214793116, 0.9635114694632674, 0.102576726650211],
    [0.18302616914497938, 0.6994976570359173, 0.3742009015937219],
    [0.23444822907046148, 0.4379649707964567, 0.20451174318655518],
    [0.6012551503462548, 0.680640618699774, 0.03079810145005235],
    [0.5607738733418359, 0.7298983704591859, 0.5221864028348002],
    [0.5246955647863423, 0.6395711438541122, 0.3213029041912717],
    [0.9327766484200443, 0.9902839397251141, 0.6688937745211762],
    [0.8003917628036332, 0.2131938170920047, 0.279066902180204],
    [0.30387223977993705, 0.12175276143691993, 0.6342167457667803],
    [0.49440500779857766, 0.6818028121638499, 0.11018758869109069],
    [0.8934945187997664, 0.25406113387803886, 0.6834885386015466],
    [0.19102254623979686, 0.4054927212995221, 0.5048932284081988],
    [0.4477981818387644, 0.16086822485097718, 0.5199581261229109],
    [0.7330380870209603, 0.1299744022984728, 0.4051750370938799],
    [0.9055282039860838, 0.6191110877678917, 0.4297605585377926],
    [0.09356862779872743, 0.8302390873728692, 0.7358499137234982],
    [0.5625926801690663, 0.29427298598691576, 0.14603018190803563],
    [0.14754438893977628, 0.27319304120106647, 0.9219791076409573],
    [0.6594564100953152, 0.21217127391400392, 0.41019793569672736],
    [0.9948656123465818, 0.03809686331076945, 0.6126499133891911],
    [0.013940936454152508, 0.6500984962176194, 0.3305515964025777],
    [0.09167413162957183, 0.6240727525012814, 0.07407170797410945],
    [0.17396860216780263, 0.5032215358840011, 0.021086059645404],
    [0.46645176998123705, 0.5040410897027042, 0.06034029147696296],
    [0.7525339863041306, 0.7972028400326427, 0.5367455404804151],
    [0.6035599584978371, 0.45497230112023157, 0.5069349898770372],
    [0.339686425154052, 0.5364857819670208, 0.9558508961723677],
    [0.8831345696403757, 0.06601207753895866, 0.4344275189600655],
    [0.2751797458253149, 0.14449330072291533, 0.6762697958554909],
    [0.9684680419976209, 0.34991147079186447, 0.22262348865146986],
    [0.18613217297389906, 0.23563412678326023, 0.9288319043082315],
    [0.04047600484938829, 0.16122690204650458, 0.6199602842180811],
    [0.10849056110149757, 0.92490900459236, 0.4549059766543232],
    [0.7232826734052815, 0.142893078579592, 0.5528635708628792],
    [0.37987615519684603, 0.17177677166364524, 0.5363696473864499],
    [0.9642949136336316, 0.25004986203773594, 0.4012307386946552],
    [0.07421552673344145, 0.2606044725534007, 0.7712934867058767],
]
limite_peso = 10
limite_volume = 10


def f(escolhidos):
    preco_total = 0
    peso_total = 0
    volume_total = 0

    for i, _ in enumerate(itens):
        if escolhidos[i] == 1:
            preco_total += itens[i][0]
            peso_total += itens[i][1]
            volume_total += itens[i][2]

    if peso_total > limite_peso:
        return 0

    if volume_total > limite_volume:
        return 0

    return preco_total


# 1
class Estado:
    def __init__(self, escolhidos):
        self.escolhidos = escolhidos
        self.f = f(escolhidos)


# 2
def estado_inicial():
    escolhidos = []
    for _ in range(len(itens)):
        escolhidos.append(random.choice([0, 1]))

    return Estado(escolhidos)


# 4
def mutacao(estado):
    escolhidos = estado.escolhidos.copy()
    i = random.randint(0, len(itens) - 1)
    escolhidos[i] = 1 - escolhidos[i]

    return Estado(escolhidos)


# 5
def cruzamento(pai1, pai2):
    escolhidos = []
    for e1, e2 in zip(pai1.escolhidos, pai2.escolhidos):
        escolhidos.append(random.choice([e1, e2]))

    return Estado(escolhidos)
