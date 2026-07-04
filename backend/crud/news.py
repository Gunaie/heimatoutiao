from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from models.news import News


async def get_news_count(db: AsyncSession, category_id: int):
    query = select(func.count(News.id)).where(News.category_id == category_id)
    result = await db.execute(query)
    return result.scalar_one()


async def increase_news_views(db: AsyncSession, news_id: int):
    query = update(News).where(News.id == news_id).values(views=News.views + 1)
    await db.execute(query)
    await db.commit()