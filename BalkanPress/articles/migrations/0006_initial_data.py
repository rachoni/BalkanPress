from django.db import migrations
from django.utils.text import slugify


def create_initial_data(apps, schema_editor):
    # 1. Get Models
    Category = apps.get_model("categories", "Category")
    Tag = apps.get_model("tags", "Tag")
    Article = apps.get_model("articles", "Article")
    Comment = apps.get_model("comments", "Comment")

    # 2. Create Categories
    categories_data = [
        "Politics",
        "Technology",
        "Sports",
        "Culture",
        "Economy",
        "Lifestyle",
        "World",
        "Health",
    ]
    categories = {}

    for name in categories_data:
        category = Category.objects.create(
            name=name,
            slug=slugify(name),
        )
        categories[name] = category

    # 3. Create Tags
    tags_data = [
        "breaking-news",
        "interview",
        "analysis",
        "opinion",
        "review",
        "health",
        "sports",
    ]
    tags = {}

    for name in tags_data:
        tag = Tag.objects.create(
            name=name,
            slug=slugify(name),
        )
        tags[name] = tag

    # 4.Create Articles
    articles_data = [
        {
            "title": "The future of AI in the Balkans",
            "summary": "How artificial intelligence is reshaping the tech landscape in the region.",
            "content": "Artificial Intelligence is no longer just a buzzword. From Sofia to Belgrade, startups are leveraging AI to solve complex problems. This article explores the growing ecosystem of AI companies in the Balkans and what it means for the future economy. We interview leading experts and look at the data driving this transformation.",
            "category": "Technology",
            "tags": ["analysis", "review"],
            "published": True,
        },
        {
            "title": "Championship Finals: A Night to Remember",
            "summary": "An In-depth look at the dramatic final match that kept everyone on the edge of their seats.",
            "content": "The stadium was packed, the energy was electric, and the match did not disappoint. In a stunning display of skill and determination, the underdogs managed to secure a victory in the final minutes. Fans are calling in the greatest match of the decade. Here is our minute-by-minute breakdown of the key plays.",
            "category": "Sports",
            "tags": ["breaking-news", "opinion", "sports"],
            "published": True,
        },
        {
            "title": "Economic Summit 2025: Key Takeways",
            "summary": "Leaders gathered to discuss inflation, trade, and regional cooperation.",
            "content": "The annual Economic Summit concluded yesterday with several major agreements signed. Key topics included energy independence, cross-border trade facilitation, and strategies to combat inflation. While some experts remain skeptical, this general sentiment is one of cautious optimism for the fiscal year ahead.",
            "category": "Economy",
            "tags": ["breaking-news", "analysis"],
            "published": True,
        },
        {
            "title": "Local Artist Wins Prestigious Award",
            "summary": "A celebration of creativity and cultural heritage.",
            "content": 'In a heartwarming ceremony last night, local painter Elena Petrova received the Golden Brush award. Her work, which blends traditional Balkan motifs with modern abstract styles, has captivated critics worldwide. "I dedicate this to my grandmother." she said in her emotional acceptance speech.',
            "category": "Culture",
            "tags": ["interview", "review"],
            "published": True,
        },
        {
            "title": "New Infrastructure Project Announced",
            "summary": "Government unveils plans for a new high-speed railway connecting major cities.",
            "content": 'The Ministry of Transport has officially announce the "Balkan Link" project. Yhis high-speed railway aims to cut travel time between capitals by half. Construction is set to begin next year, with funding secured from both local and international partners. Environmentalists have raised some concerns, but the government promises a green approach.',
            "category": "Politics",
            "tags": ["breaking-news"],
            "published": True,
        },
        {
            "title": "AI Revolution in Balkan Healthcare",
            "summary": "New AI-driven diagnostics are saving lives in local hospitals.",
            "content": "A groundbreaking collaboration between tech startups and medical institutions is  transforming patient care. By utilizing advanced machine learning algorithms, doctors can now detect early signs of diseases with unprecendeted accuracy. This article delves into the specific technologies being deployed and the impact on public health across the region.",
            "categories": ["Technology", "Health"],
            "tags": ["breaking-news", "analysis"],
            "published": True,
        },
    ]

    created_articles = []
    for data in articles_data:
        article = Article.objects.create(
            title=data["title"],
            summary=data["summary"],
            content=data["content"],
            is_published=data["published"],
            # Slug is usually handled by save() method, but in migrations save() logic isn't always triggered automatically depending on implementation.
            # However, since we use apps.get_model, we don't have access to custom save() methods easily.
            # We should manually set the slug here to be safe.
            slug=slugify(f"{data['title']}"),
        )

        # Add Many-to-Many relationships
        # Handle 'categories' (list) if present
        if "categories" in data:
            for cat_name in data["categories"]:
                article.categories.add(categories[cat_name])
        # Handle 'category' (single string) if present
        elif "category" in data:
            article.categories.add(categories[data["category"]])

        for tag_name in data["tags"]:
            article.tags.add(tags[tag_name])

        created_articles.append(article)

    # 5. Create Comments
    comments_data = [
        {
            "article_index": 0,  # AI article
            "author": "TechEnthusiast",
            "body": "Great read! The potential is huge.",
            "approved": True,
        },
        {
            "article_index": 0,
            "author": "Skeptic101",
            "body": "I am worried about job displacement though.",
            "approved": True,
        },
        {
            "article_index": 1,  # Sports article
            "author": "FanBoy",
            "body": "What a game! Unbelievable!",
            "approved": True,
        },
        {
            "article_index": 2,  # Economy
            "author": "Economist",
            "body": "Inflation is still the biggest issue.",
            "approved": False,
        },
    ]

    for c_data in comments_data:
        Comment.objects.create(
            article=created_articles[c_data["article_index"]],
            author_name=c_data["author"],
            body=c_data["body"],
            is_approved=c_data["approved"],
        )


def reverse_initial_data(apps, schema_editor):
    # Logic to delete data if we unapply the migration
    Category = apps.get_model("categories", "Category")
    Tag = apps.get_model("tags", "Tag")
    Article = apps.get_model("articles", "Article")
    Comment = apps.get_model("comments", "Comment")

    Comment.objects.all().delete()
    Article.objects.all().delete()
    Tag.objects.all().delete()
    Category.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        (
            "articles",
            "0005_alter_article_featured_image",
        ),  # Replace with the actual last migration name of articles app
        ("categories", "0003_alter_category_options"),
        ("tags", "0002_alter_tag_slug"),
        ("comments", "0002_alter_comment_options_remove_comment_is_published_and_more"),
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_initial_data),
    ]
