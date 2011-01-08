# Extra stress testing for Bessel functions
# Reference zeros generated with the aid of scipy.special
# jn_zero, jnp_zero, yn_zero, ynp_zero

from mpmath import *

V = 15
M = 15

jn_small_zeros = \
[[2.4048255576957728,
  5.5200781102863106,
  8.6537279129110122,
  11.791534439014282,
  14.930917708487786,
  18.071063967910923,
  21.211636629879259,
  24.352471530749303,
  27.493479132040255,
  30.634606468431975,
  33.775820213573569,
  36.917098353664044,
  40.058425764628239,
  43.19979171317673,
  46.341188371661814],
 [3.8317059702075123,
  7.0155866698156188,
  10.173468135062722,
  13.323691936314223,
  16.470630050877633,
  19.615858510468242,
  22.760084380592772,
  25.903672087618383,
  29.046828534916855,
  32.189679910974404,
  35.332307550083865,
  38.474766234771615,
  41.617094212814451,
  44.759318997652822,
  47.901460887185447],
 [5.1356223018406826,
  8.4172441403998649,
  11.619841172149059,
  14.795951782351261,
  17.959819494987826,
  21.116997053021846,
  24.270112313573103,
  27.420573549984557,
  30.569204495516397,
  33.7165195092227,
  36.86285651128381,
  40.008446733478192,
  43.153453778371463,
  46.297996677236919,
  49.442164110416873],
 [6.3801618959239835,
  9.7610231299816697,
  13.015200721698434,
  16.223466160318768,
  19.409415226435012,
  22.582729593104442,
  25.748166699294978,
  28.908350780921758,
  32.064852407097709,
  35.218670738610115,
  38.370472434756944,
  41.520719670406776,
  44.669743116617253,
  47.817785691533302,
  50.965029906205183],
 [7.5883424345038044,
  11.064709488501185,
  14.37253667161759,
  17.615966049804833,
  20.826932956962388,
  24.01901952477111,
  27.199087765981251,
  30.371007667117247,
  33.537137711819223,
  36.699001128744649,
  39.857627302180889,
  43.01373772335443,
  46.167853512924375,
  49.320360686390272,
  52.471551398458023],
 [8.771483815959954,
  12.338604197466944,
  15.700174079711671,
  18.980133875179921,
  22.217799896561268,
  25.430341154222704,
  28.626618307291138,
  31.811716724047763,
  34.988781294559295,
  38.159868561967132,
  41.326383254047406,
  44.489319123219673,
  47.649399806697054,
  50.80716520300633,
  53.963026558378149],
 [9.9361095242176849,
  13.589290170541217,
  17.003819667816014,
  20.320789213566506,
  23.58608443558139,
  26.820151983411405,
  30.033722386570469,
  33.233041762847123,
  36.422019668258457,
  39.603239416075404,
  42.778481613199507,
  45.949015998042603,
  49.11577372476426,
  52.279453903601052,
  55.440592068853149],
 [11.086370019245084,
  14.821268727013171,
  18.287582832481726,
  21.641541019848401,
  24.934927887673022,
  28.191188459483199,
  31.42279419226558,
  34.637089352069324,
  37.838717382853611,
  41.030773691585537,
  44.21540850526126,
  47.394165755570512,
  50.568184679795566,
  53.738325371963291,
  56.905249991978781],
 [12.225092264004655,
  16.037774190887709,
  19.554536430997055,
  22.94517313187462,
  26.266814641176644,
  29.54565967099855,
  32.795800037341462,
  36.025615063869571,
  39.240447995178135,
  42.443887743273558,
  45.638444182199141,
  48.825930381553857,
  52.007691456686903,
  55.184747939289049,
  58.357889025269694],
 [13.354300477435331,
  17.241220382489128,
  20.807047789264107,
  24.233885257750552,
  27.583748963573006,
  30.885378967696675,
  34.154377923855096,
  37.400099977156589,
  40.628553718964528,
  43.843801420337347,
  47.048700737654032,
  50.245326955305383,
  53.435227157042058,
  56.619580266508436,
  59.799301630960228],
 [14.475500686554541,
  18.433463666966583,
  22.046985364697802,
  25.509450554182826,
  28.887375063530457,
  32.211856199712731,
  35.499909205373851,
  38.761807017881651,
  42.004190236671805,
  45.231574103535045,
  48.447151387269394,
  51.653251668165858,
  54.851619075963349,
  58.043587928232478,
  61.230197977292681],
 [15.589847884455485,
  19.61596690396692,
  23.275853726263409,
  26.773322545509539,
  30.17906117878486,
  33.526364075588624,
  36.833571341894905,
  40.111823270954241,
  43.368360947521711,
  46.608132676274944,
  49.834653510396724,
  53.050498959135054,
  56.257604715114484,
  59.457456908388002,
  62.651217388202912],
 [16.698249933848246,
  20.789906360078443,
  24.494885043881354,
  28.026709949973129,
  31.45996003531804,
  34.829986990290238,
  38.156377504681354,
  41.451092307939681,
  44.721943543191147,
  47.974293531269048,
  51.211967004101068,
  54.437776928325074,
  57.653844811906946,
  60.8618046824805,
  64.062937824850136],
 [17.801435153282442,
  21.95624406783631,
  25.705103053924724,
  29.270630441874802,
  32.731053310978403,
  36.123657666448762,
  39.469206825243883,
  42.780439265447158,
  46.06571091157561,
  49.330780096443524,
  52.579769064383396,
  55.815719876305778,
  59.040934037249271,
  62.257189393731728,
  65.465883797232125],
 [18.899997953174024,
  23.115778347252756,
  26.907368976182104,
  30.505950163896036,
  33.993184984781542,
  37.408185128639695,
  40.772827853501868,
  44.100590565798301,
  47.400347780543231,
  50.678236946479898,
  53.93866620912693,
  57.184898598119301,
  60.419409852130297,
  63.644117508962281,
  66.860533012260103]]

jnp_small_zeros = \
[[0.0,
  3.8317059702075123,
  7.0155866698156188,
  10.173468135062722,
  13.323691936314223,
  16.470630050877633,
  19.615858510468242,
  22.760084380592772,
  25.903672087618383,
  29.046828534916855,
  32.189679910974404,
  35.332307550083865,
  38.474766234771615,
  41.617094212814451,
  44.759318997652822],
 [1.8411837813406593,
  5.3314427735250326,
  8.5363163663462858,
  11.706004902592064,
  14.863588633909033,
  18.015527862681804,
  21.16436985918879,
  24.311326857210776,
  27.457050571059246,
  30.601922972669094,
  33.746182898667383,
  36.889987409236811,
  40.033444053350675,
  43.176628965448822,
  46.319597561173912],
 [3.0542369282271403,
  6.7061331941584591,
  9.9694678230875958,
  13.170370856016123,
  16.347522318321783,
  19.512912782488205,
  22.671581772477426,
  25.826037141785263,
  28.977672772993679,
  32.127327020443474,
  35.275535050674691,
  38.422654817555906,
  41.568934936074314,
  44.714553532819734,
  47.859641607992093],
 [4.2011889412105285,
  8.0152365983759522,
  11.345924310743006,
  14.585848286167028,
  17.78874786606647,
  20.9724769365377,
  24.144897432909265,
  27.310057930204349,
  30.470268806290424,
  33.626949182796679,
  36.781020675464386,
  39.933108623659488,
  43.083652662375079,
  46.232971081836478,
  49.381300092370349],
 [5.3175531260839944,
  9.2823962852416123,
  12.681908442638891,
  15.964107037731551,
  19.196028800048905,
  22.401032267689004,
  25.589759681386733,
  28.767836217666503,
  31.938539340972783,
  35.103916677346764,
  38.265316987088158,
  41.423666498500732,
  44.579623137359257,
  47.733667523865744,
  50.886159153182682],
 [6.4156163757002403,
  10.519860873772308,
  13.9871886301403,
  17.312842487884625,
  20.575514521386888,
  23.803581476593863,
  27.01030789777772,
  30.20284907898166,
  33.385443901010121,
  36.560777686880356,
  39.730640230067416,
  42.896273163494417,
  46.058566273567043,
  49.218174614666636,
  52.375591529563596],
 [7.501266144684147,
  11.734935953042708,
  15.268181461097873,
  18.637443009666202,
  21.931715017802236,
  25.183925599499626,
  28.409776362510085,
  31.617875716105035,
  34.81339298429743,
  37.999640897715301,
  41.178849474321413,
  44.352579199070217,
  47.521956905768113,
  50.687817781723741,
  53.85079463676896],
 [8.5778364897140741,
  12.932386237089576,
  16.529365884366944,
  19.941853366527342,
  23.268052926457571,
  26.545032061823576,
  29.790748583196614,
  33.015178641375142,
  36.224380548787162,
  39.422274578939259,
  42.611522172286684,
  45.793999658055002,
  48.971070951900596,
  52.143752969301988,
  55.312820330403446],
 [9.6474216519972168,
  14.115518907894618,
  17.774012366915256,
  21.229062622853124,
  24.587197486317681,
  27.889269427955092,
  31.155326556188325,
  34.39662855427218,
  37.620078044197086,
  40.830178681822041,
  44.030010337966153,
  47.221758471887113,
  50.407020967034367,
  53.586995435398319,
  56.762598475105272],
 [10.711433970699945,
  15.28673766733295,
  19.004593537946053,
  22.501398726777283,
  25.891277276839136,
  29.218563499936081,
  32.505247352375523,
  35.763792928808799,
  39.001902811514218,
  42.224638430753279,
  45.435483097475542,
  48.636922645305525,
  51.830783925834728,
  55.01844255063594,
  58.200955824859509],
 [11.770876674955582,
  16.447852748486498,
  20.223031412681701,
  23.760715860327448,
  27.182021527190532,
  30.534504754007074,
  33.841965775135715,
  37.118000423665604,
  40.371068905333891,
  43.606764901379516,
  46.828959446564562,
  50.040428970943456,
  53.243223214220535,
  56.438892058982552,
  59.628631306921512],
 [12.826491228033465,
  17.600266557468326,
  21.430854238060294,
  25.008518704644261,
  28.460857279654847,
  31.838424458616998,
  35.166714427392629,
  38.460388720328256,
  41.728625562624312,
  44.977526250903469,
  48.211333836373288,
  51.433105171422278,
  54.645106240447105,
  57.849056857839799,
  61.046288512821078],
 [13.878843069697276,
  18.745090916814406,
  22.629300302835503,
  26.246047773946584,
  29.72897816891134,
  33.131449953571661,
  36.480548302231658,
  39.791940718940855,
  43.075486800191012,
  46.337772104541405,
  49.583396417633095,
  52.815686826850452,
  56.037118687012179,
  59.249577075517968,
  62.454525995970462],
 [14.928374492964716,
  19.88322436109951,
  23.81938909003628,
  27.474339750968247,
  30.987394331665278,
  34.414545662167183,
  37.784378506209499,
  41.113512376883377,
  44.412454519229281,
  47.688252845993366,
  50.945849245830813,
  54.188831071035124,
  57.419876154678179,
  60.641030026538746,
  63.853885828967512],
 [15.975438807484321,
  21.015404934568315,
  25.001971500138194,
  28.694271223110755,
  32.236969407878118,
  35.688544091185301,
  39.078998185245057,
  42.425854432866141,
  45.740236776624833,
  49.029635055514276,
  52.299319390331728,
  55.553127779547459,
  58.793933759028134,
  62.02393848337554,
  65.244860767043859]]

yn_small_zeros = \
[[0.89357696627916752,
  3.9576784193148579,
  7.0860510603017727,
  10.222345043496417,
  13.361097473872763,
  16.500922441528091,
  19.64130970088794,
  22.782028047291559,
  25.922957653180923,
  29.064030252728398,
  32.205204116493281,
  35.346452305214321,
  38.487756653081537,
  41.629104466213808,
  44.770486607221993],
 [2.197141326031017,
  5.4296810407941351,
  8.5960058683311689,
  11.749154830839881,
  14.897442128336725,
  18.043402276727856,
  21.188068934142213,
  24.331942571356912,
  27.475294980449224,
  30.618286491641115,
  33.761017796109326,
  36.90355531614295,
  40.045944640266876,
  43.188218097393211,
  46.330399250701687],
 [3.3842417671495935,
  6.7938075132682675,
  10.023477979360038,
  13.209986710206416,
  16.378966558947457,
  19.539039990286384,
  22.69395593890929,
  25.845613720902269,
  28.995080395650151,
  32.143002257627551,
  35.289793869635804,
  38.435733485446343,
  41.581014867297885,
  44.725777117640461,
  47.870122696676504],
 [4.5270246611496439,
  8.0975537628604907,
  11.396466739595867,
  14.623077742393873,
  17.81845523294552,
  20.997284754187761,
  24.166235758581828,
  27.328799850405162,
  30.486989604098659,
  33.642049384702463,
  36.794791029185579,
  39.945767226378749,
  43.095367507846703,
  46.2438744334407,
  49.391498015725107],
 [5.6451478942208959,
  9.3616206152445429,
  12.730144474090465,
  15.999627085382479,
  19.22442895931681,
  22.424810599698521,
  25.610267054939328,
  28.785893657666548,
  31.954686680031668,
  35.118529525584828,
  38.278668089521758,
  41.435960629910073,
  44.591018225353424,
  47.744288086361052,
  50.896105199722123],
 [6.7471838248710219,
  10.597176726782031,
  14.033804104911233,
  17.347086393228382,
  20.602899017175335,
  23.826536030287532,
  27.030134937138834,
  30.220335654231385,
  33.401105611047908,
  36.574972486670962,
  39.743627733020277,
  42.908248189569535,
  46.069679073215439,
  49.228543693445843,
  52.385312123112282],
 [7.8377378223268716,
  11.811037107609447,
  15.313615118517857,
  18.670704965906724,
  21.958290897126571,
  25.206207715021249,
  28.429037095235496,
  31.634879502950644,
  34.828638524084437,
  38.013473399691765,
  41.19151880917741,
  44.364272633271975,
  47.53281875312084,
  50.697961822183806,
  53.860312300118388],
 [8.919605734873789,
  13.007711435388313,
  16.573915129085334,
  19.974342312352426,
  23.293972585596648,
  26.5667563757203,
  29.809531451608321,
  33.031769327150685,
  36.239265816598239,
  39.435790312675323,
  42.623910919472727,
  45.805442883111651,
  48.981708325514764,
  52.153694518185572,
  55.322154420959698],
 [9.9946283820824834,
  14.190361295800141,
  17.817887841179873,
  21.26093227125945,
  24.612576377421522,
  27.910524883974868,
  31.173701563441602,
  34.412862242025045,
  37.634648706110989,
  40.843415321050884,
  44.04214994542435,
  47.232978012841169,
  50.417456447370186,
  53.596753874948731,
  56.771765754432457],
 [11.064090256031013,
  15.361301343575925,
  19.047949646361388,
  22.532765416313869,
  25.91620496332662,
  29.2394205079349,
  32.523270869465881,
  35.779715464475261,
  39.016196664616095,
  42.237627509803703,
  45.4474001519274,
  48.647941127433196,
  51.841036928216499,
  55.028034667184916,
  58.209970905250097],
 [12.128927704415439,
  16.522284394784426,
  20.265984501212254,
  23.791669719454272,
  27.206568881574774,
  30.555020011020762,
  33.859683872746356,
  37.133649760307504,
  40.385117593813002,
  43.619533085646856,
  46.840676630553575,
  50.051265851897857,
  53.253310556711732,
  56.448332488918971,
  59.637507005589829],
 [13.189846995683845,
  17.674674253171487,
  21.473493977824902,
  25.03913093040942,
  28.485081336558058,
  31.858644293774859,
  35.184165245422787,
  38.475796636190897,
  41.742455848758449,
  44.990096293791186,
  48.222870660068338,
  51.443777308699826,
  54.655042589416311,
  57.858358441436511,
  61.055036135780528],
 [14.247395665073945,
  18.819555894710682,
  22.671697117872794,
  26.276375544903892,
  29.752925495549038,
  33.151412708998983,
  36.497763772987645,
  39.807134090704376,
  43.089121522203808,
  46.350163579538652,
  49.594769786270069,
  52.82620892320143,
  56.046916910756961,
  59.258751140598783,
  62.463155567737854],
 [15.30200785858925,
  19.957808654258601,
  23.861599172945054,
  27.504429642227545,
  31.011103429019229,
  34.434283425782942,
  37.801385632318459,
  41.128514139788358,
  44.425913324440663,
  47.700482714581842,
  50.957073905278458,
  54.199216028087261,
  57.429547607017405,
  60.65008661807661,
  63.862406280068586],
 [16.354034360047551,
  21.090156519983806,
  25.044040298785627,
  28.724161640881914,
  32.260472459522644,
  35.708083982611664,
  39.095820003878235,
  42.440684315990936,
  45.75353669045622,
  49.041718113283529,
  52.310408280968073,
  55.56338698149062,
  58.803488508906895,
  62.032886550960831,
  65.253280088312461]]

ynp_small_zeros = \
[[2.197141326031017,
  5.4296810407941351,
  8.5960058683311689,
  11.749154830839881,
  14.897442128336725,
  18.043402276727856,
  21.188068934142213,
  24.331942571356912,
  27.475294980449224,
  30.618286491641115,
  33.761017796109326,
  36.90355531614295,
  40.045944640266876,
  43.188218097393211,
  46.330399250701687],
 [3.6830228565851777,
  6.9414999536541757,
  10.123404655436613,
  13.285758156782854,
  16.440058007293282,
  19.590241756629495,
  22.738034717396327,
  25.884314618788867,
  29.029575819372535,
  32.174118233366201,
  35.318134458192094,
  38.461753870997549,
  41.605066618873108,
  44.74813744908079,
  47.891014070791065],
 [5.0025829314460639,
  8.3507247014130795,
  11.574195465217647,
  14.760909306207676,
  17.931285939466855,
  21.092894504412739,
  24.249231678519058,
  27.402145837145258,
  30.552708880564553,
  33.70158627151572,
  36.849213419846257,
  39.995887376143356,
  43.141817835750686,
  46.287157097544201,
  49.432018469138281],
 [6.2536332084598136,
  9.6987879841487711,
  12.972409052292216,
  16.19044719506921,
  19.38238844973613,
  22.559791857764261,
  25.728213194724094,
  28.890678419054777,
  32.048984005266337,
  35.204266606440635,
  38.357281675961019,
  41.508551443818436,
  44.658448731963676,
  47.807246956681162,
  50.95515126455207],
 [7.4649217367571329,
  11.005169149809189,
  14.3317235192331,
  17.58443601710272,
  20.801062338411128,
  23.997004122902644,
  27.179886689853435,
  30.353960608554323,
  33.521797098666792,
  36.685048382072301,
  39.844826969405863,
  43.001910515625288,
  46.15685955107263,
  49.310088614282257,
  52.461911043685864],
 [8.6495562436971983,
  12.280868725807848,
  15.660799304540377,
  18.949739756016503,
  22.192841809428241,
  25.409072788867674,
  28.608039283077593,
  31.795195353138159,
  34.973890634255288,
  38.14630522169358,
  41.313923188794905,
  44.477791768537617,
  47.638672065035628,
  50.797131066967842,
  53.953600129601663],
 [9.8147970120105779,
  13.532811875789828,
  16.965526446046053,
  20.291285512443867,
  23.56186260680065,
  26.799499736027237,
  30.015665481543419,
  33.216968050039509,
  36.407516858984748,
  39.590015243560459,
  42.766320595957378,
  45.937754257017323,
  49.105283450953203,
  52.269633324547373,
  55.431358715604255],
 [10.965152105242974,
  14.765687379508912,
  18.250123150217555,
  21.612750053384621,
  24.911310600813573,
  28.171051927637585,
  31.40518108895689,
  34.621401012564177,
  37.824552065973114,
  41.017847386464902,
  44.203512240871601,
  47.3831408366063,
  50.557907466622796,
  53.728697478957026,
  56.896191727313342],
 [12.103641941939539,
  15.982840905145284,
  19.517731005559611,
  22.916962141504605,
  26.243700855690533,
  29.525960140695407,
  32.778568197561124,
  36.010261572392516,
  39.226578757802172,
  42.43122493258747,
  45.626783824134354,
  48.815117837929515,
  51.997606404328863,
  55.175294723956816,
  58.348990221754937],
 [13.232403808592215,
  17.186756572616758,
  20.770762917490496,
  24.206152448722253,
  27.561059462697153,
  30.866053571250639,
  34.137476603379774,
  37.385039772270268,
  40.614946085165892,
  43.831373184731238,
  47.037251786726299,
  50.234705848765229,
  53.425316228549359,
  56.610286079882087,
  59.790548623216652],
 [14.35301374369987,
  18.379337301642568,
  22.011118775283494,
  25.482116178696707,
  28.865046588695164,
  32.192853922166294,
  35.483296655830277,
  38.747005493021857,
  41.990815194320955,
  45.219355876831731,
  48.435892856078888,
  51.642803925173029,
  54.84186659475857,
  58.034439083840155,
  61.221578745109862],
 [15.466672066554263,
  19.562077985759503,
  23.240325531101082,
  26.746322986645901,
  30.157042415639891,
  33.507642948240263,
  36.817212798512775,
  40.097251300178642,
  43.355193847719752,
  46.596103410173672,
  49.823567279972794,
  53.040208868780832,
  56.247996968470062,
  59.448441365714251,
  62.642721301357187],
 [16.574317035530872,
  20.73617763753932,
  24.459631728238804,
  27.999993668839644,
  31.438208790267783,
  34.811512070805535,
  38.140243708611251,
  41.436725143893739,
  44.708963264433333,
  47.962435051891027,
  51.201037321915983,
  54.427630745992975,
  57.644369734615238,
  60.852911791989989,
  64.054555435720397],
 [17.676697936439624,
  21.9026148697762,
  25.670073356263225,
  29.244155124266438,
  32.709534477396028,
  36.105399554497548,
  39.453272918267025,
  42.766255701958017,
  46.052899215578358,
  49.319076602061401,
  52.568982147952547,
  55.805705507386287,
  59.031580956740466,
  62.248409689597653,
  65.457606670836759],
 [18.774423978290318,
  23.06220035979272,
  26.872520985976736,
  30.479680663499762,
  33.971869047372436,
  37.390118854896324,
  40.757072537673599,
  44.086572292170345,
  47.387688809191869,
  50.66667461073936,
  53.928009929563275,
  57.175005343085052,
  60.410169281219877,
  63.635442539153021,
  66.85235358587768]]

def test_bessel_zeros():
    mp.dps = 15
    for v in range(V):
        for m in range(1,M+1):
            print(v, m, "of", V, M)
            # Twice to test cache (if used)
            assert besseljzero(v,m).ae(jn_small_zeros[v][m-1])
            assert besseljzero(v,m).ae(jn_small_zeros[v][m-1])
            assert besseljzero(v,m,1).ae(jnp_small_zeros[v][m-1])
            assert besseljzero(v,m,1).ae(jnp_small_zeros[v][m-1])
            assert besselyzero(v,m).ae(yn_small_zeros[v][m-1])
            assert besselyzero(v,m).ae(yn_small_zeros[v][m-1])
            assert besselyzero(v,m,1).ae(ynp_small_zeros[v][m-1])
            assert besselyzero(v,m,1).ae(ynp_small_zeros[v][m-1])

if __name__ == "__main__":
    test_bessel_zeros()
