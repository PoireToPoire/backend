import json
from datetime import datetime

from fastapi import APIRouter
from lib.db import mysql_connection
from lib.http_handle import handle_errors

router = APIRouter(
    prefix="/posts",
    tags=["post"],
    responses={404: {"description": "Not found"}},
)

db = mysql_connection()


@router.get("/{post_id}")
def get_post(post_id: int):
    with handle_errors():
        post = db.find_post_by_id(post_id)
    return json.dumps(post, indent=4, sort_keys=True, default=str)


@router.get("")
def get_posts():
    return {
        # Structure fonctionnelle dans l'app flutter
        0: {
            "title": "Bonjour tout le monde",
            "content": "Cillum consectetur id culpa id ut. Eiusmod veniam adipisicing voluptate consequat elit aute Lorem ex dolor consequat reprehenderit ea. Do labore voluptate incididunt duis irure excepteur ea. Sit elit ea quis aute exercitation dolor ut commodo elit ullamco nulla esse deserunt. Pariatur occaecat labore sit culpa aliquip tempor non et labore reprehenderit consectetur amet ut Lorem. Non ea eiusmod occaecat sit dolore enim. Do nisi commodo non quis adipisicing nisi irure commodo voluptate ad ex.",
            "date": datetime.now(),
            "picture": "https://images.unsplash.com/photo-1613560774329-9bb0682a85e9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
            "likes": 59,
        },
        1: {
            "title": "Ceci est un second article",
            "content": "il y a pas vraiment de contenu",
            "date": datetime.now(),
            "picture": "https://images.unsplash.com/photo-1613553914536-eec5a84ae9a7?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=750&q=80",
            "likes": 204,
        },
        2: {
            "title": "Un troisième article..",
            "content": "BlaBlaBla",
            "date": datetime.now(),
            "picture": "https://images.unsplash.com/photo-1593642634443-44adaa06623a?ixid=MXwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=625&q=80",
            "likes": 23,
        },
    }
