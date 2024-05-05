import pytest 

from blog.models import Article
from blog.commands import CreateArticleCommand, AlereadyExists

def test_create_article():
    """
    GIVEN CreateArticleCommand with valid author, title, and content properties
    WHEN the execute method is called
    THEN a new Article must exist in the database with the same attributes
    """
    cmd = CreateArticleCommand(
        author="carlos@doe.com",
        title="New Article",
        content="Super Awesome Article"
    )

    article = cmd.execute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content
    

def test_create_article_already_exists():
    """ Pattern for writing good tests(Arrange,Act,Assert)
    GIVEN CreateArticleCommand with some article in database
    WHEN the execute method is called
    THEN a new Article must exist in the database with the same attributes
    """

    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super Extra Awesome Article"
    ).save()

    cmd = CreateArticleCommand(
        author="carlos@doe.com",
        title="New Article",
        content="Super Awesome Article"
    )

    with pytest.raises(AlereadyExists):
        cmd.execute()