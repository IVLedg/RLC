import sys, os, core, settings

from lib.logger import logger

__version__ = settings.VERSION
__author__ = settings.AUTHOR

def header():
    os.system("clear")
    
    print ('''
                                                 ae
                          .___   ]@@
                      _zza@@@@@bd@@@ _
                ]@L._d@@@@@@@@@@@@@@a[
                `@@@@@@@@@@@@@@@@@@@@[
             __zd@@@@@@@@@@@@@@@@@@@@
             "~]@@@@@@zzd@@@@@@@@@@@@
               q@@@@~_a@@@@@@~@@@@@@@,
               ]@@~ _a@@@@@~@b ]@@@@@
              _@]bz@~"     _@@ ]@@@~
              @~UCL______z%~  .a@@@,
              qz "~~~~~~"    _a@@@@L
.___,          `z_,        _d@@@@@@@bL____
dC~~-zz_ ._    ]d@@@z_   .d@@@@@@@@@@@@@@@@L
`~@zL_"~-@]b_,z@@@@@@@b__a@@@@@@@@@@@@@@@@@@,
   `~~aza'  `~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[
       ][    .d@-@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .%    ]a@z__"~~@@@@@@@@@@@@@@@@@@@@@@@@,
      d'  .d@@@@@@@zz__~~-@@@@@@@@@@@@@@@@@@@'
     ]P  ]@@@@@@@@@@@@@@z__"~-@@@@@@@@@@@@@@@,
    dr  )@@@@@@@@@@@@@@@@@@@zz_`~~@@@@@@@@@@@L
   d'   d@@@@@@@@@@@@@@@@@@@@@@@bzL=~~@@@@@@@L
  d'    a@@@@@' `@@@@@@@@@@@@@@@@@@@@zz_~~~@@@~-zz_
 d'    ]@@@@@'   ]@@@@@@@@@@@@@@@@@@@@@@@zz_]r.% _~a_         _d~-_
.[     a@@@~     ]@@@@@@@@@@@@@@@@@@@@@@@@@@@Ld'.[.%az__  __z="   ~-_
][    )@@@'      `@@@@@@@@@@@@@@@@@@@@@@@@~~~@@_d'aCC`~~~~~"  ____ `~z_
]'    a@@        .@@@@@@@@@@@@@@@@@@@@@@P     `]@~~~~~zz     `@=~~@z_`~z@,
]    d@~'        ]@@@@@@@@@@@@@@@@@@@@@@      _r       qL      ~-z_]7-z_~@
],._d'          .a@@@@@@@@@@@@@@@@@@@@@[    _d'        `a  )zzL_,`~U@z@bza
]b~~            d@@@@@@@@@@@@@@@@@@@@@@@__zd~'          ]L  a_`~~-zL"~z  ~
                a@@@@@@@@@@@@@@@@@@@@@@@~"               a, "~-z_`-z--=-
               .@@@@@@@@@@@@@@@@@@@@@@@@b                `L__  `~-d@z
               ]@@@@@@@@@@@@@@@@@@@@@@@@@,                "~~~~-zz_"`L
              ]@@@@@@@@@@@@@@@@@@@@@@@@@@L                      `~K~~~'
             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@b_                       ╦╦  ╦                                             
                `~~~~~~~~-@@@@@@@@@@@@@@@@@@bL                     ║╚╗╔╝
                               ~~~~~~~~~@@@@@@@L                   ╩ ╚╝o
                                                                 ╦═╗╦  ╔═╗
                                                                 ╠╦╝║  ║ 
                                                                 ╩╚═╩═╝╚═╝o
             ''')
    
   
def showhelp():
    print ('''
    Usage: python RLC.py [Name] [Output]
    Target:
        -n, --name FIVEM      Target FiveM ID
        
    Options:
        -h, --help                Show basic help message
        -v, --version             Show program's version number
        -u, --update              Update program from repository
        
    Output: 
        -o, --output file         Print log on a file
    Examples:
        python RLC.py -n name
        python RLC.py -n name -o
        python RLC.py -u
    ''')     

def resolve(name):
    ip = core.get_ip_by_name(name)
    msg = ip
    if msg:
        logger.info('[+] Resolved!  IP: ' + msg)
    else:
        logger.error('[-] Error: Impossible to resolve ' + name)















#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.