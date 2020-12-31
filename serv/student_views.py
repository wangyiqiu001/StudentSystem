from aiohttp import web
from aiohttp.web_request import Request
from .config import db_block, web_routes, render_html
from .utils import login_required

@web_routes.get("/student")
@login_required
async def view_student_list(request):
    return render_html(request, 'student_list.html')
