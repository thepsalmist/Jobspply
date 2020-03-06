from django.utils.text import slugify


def slug_generator(model_instance, title, slug_field):
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class.objects.filter(slug=slug).exists():
        # create
        object_pk = model_class.objects.latest("pk")
        object_pk = object_pk + 1

        slug = f"{slug}-{object_pk}"

    return slug
