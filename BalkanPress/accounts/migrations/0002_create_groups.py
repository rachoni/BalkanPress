from django.db import migrations


def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    # Groups
    authors_group, _ = Group.objects.get_or_create(name="Authors")
    moderators_group, _ = Group.objects.get_or_create(name="Moderators")

    # Permissions by codename
    # Article
    article_perms = Permission.objects.filter(
        codename__in=[
            "add_article",
            "change_article",
            "delete_article",
            "view_article",
        ]
    )

    # Comment (moderation)
    comment_perms = Permission.objects.filter(
        codename__in=[
            "add_comment",
            "change_comment",
            "delete_comment",
            "view_comment",
        ]
    )

    # Category
    category_perms = Permission.objects.filter(
        codename__in=[
            "add_category",
            "change_category",
            "delete_category",
            "view_category",
        ]
    )

    # Tag
    tag_perms = Permission.objects.filter(
        codename__in=[
            "add_tag",
            "change_tag",
            "delete_tag",
            "view_tag",
        ]
    )

    # Authors:all article perms + + add/change/view tag + add/change/view comment
    authors_group.permissions.set(
        article_perms
        | tag_perms.filter(
            codename__in=[
                "add_tag",
                "change_tag",
                "view_tag",
            ]
        )
        | comment_perms.filter(
            codename__in=[
                "add_comment",
                "change_comment",
                "view_comment",
            ]
        )
    )

    # Moderators: full control of articles, comments, categories, tags
    moderators_group.permissions.set(
        article_perms | comment_perms | category_perms | tag_perms
    )


def remove_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Authors", "Moderators"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions, remove_groups),
    ]
