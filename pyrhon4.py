from django_micro import configure, route, run
from django.http import HttpResponse
from parts import table

import csv

DEBUG = True
LANGUAGE_COOE = "en-us"

configure(locals)

@route('',name='home')
def homepage(request):
    html = f'''
    <div style="background-color:#0A0A0E;height:100%">
        <image src="https://file-rctyjgetlr.now.sh" style="height:70%;margin:auto;display:block">
        <table style="width:60%；color:white;border-collapse:collapse" align="center">
            {table}
        </table>
    </div>'''

    return HttpResponse(html)

application = run()

#
# table = f'''
#     <tr style="border-top:1pt solid #555555">
#         <td><h3> APR 6 </h3></td>
#         <td><h3> PNC ARENA</h3></td>
#         <td><h3> RALEIGH, NC</h3></td>
#     </tr>
#
#     <tr style="border-top:1pt solid #555555">
#         <td><h3> ARP 7 </h3></td>
#         <td><h3> STATE FARM ARENA</h3></td>
#         <td><h3> ATLANTA, GA</h3></td>
#     </tr>
#
#     <tr style="border-top:1pt solid #555555">
#         <td><h3> APR 9 </h3></td>
#         <td><h3> BRIDGESTONE ARENA</h3></td>
#         <td><h3> NASHVILLE, TN</h3></td>
#     </tr>
#
#     <tr style="border-top:1pt solid #555555">
#         <td><h3> APR 11 </h3></td>
#         <td><h3> AMALIE ARENA</h3></td>
#         <td><h3> TAMPA, FL</h3></td>
#     </tr>'''
