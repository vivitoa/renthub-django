from django.core.management.base import BaseCommand
from catalog.models import Category, Item


class Command(BaseCommand):
    help = 'Seeds the database with initial categories and items for testing.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning database...")
        Item.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write("Starting database seeding...")

        categories_data = ['Electronics', 'Tools', 'Vehicles', 'Party Equipment']
        categories = {}

        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(name=cat_name)
            categories[cat_name] = category
            if created:
                self.stdout.write(f"Created category: {cat_name}")

        items_data = [
            {
                'title': 'Sony PlayStation 5',
                'description': 'Next-gen gaming console with one DualSense controller included. Perfect for a weekend gaming session.',
                'price_per_day': 15.00,
                'image_url': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=800',
                'category': categories['Electronics']
            },
            {
                'title': 'Bosch Professional Power Drill',
                'description': 'Heavy-duty impact drill for concrete and wood. Includes a set of basic drill bits.',
                'price_per_day': 8.50,
                'image_url': 'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800',
                'category': categories['Tools']
            },
            {
                'title': 'Electric Scooter Xiaomi Pro 2',
                'description': 'Fast and reliable electric scooter with up to 45km range. Helmet included. Great for city commuting.',
                'price_per_day': 20.00,
                'image_url': 'https://primary.jwwb.nl/public/v/d/m/temp-glwkioydlpcpzdigbzlu/7vxlpw/image-2.png',
                'category': categories['Vehicles']
            },
            {
                'title': 'Professional Karaoke Speaker',
                'description': 'High-power Bluetooth speaker with RGB lights and two wireless microphones. Perfect for parties.',
                'price_per_day': 25.00,
                'image_url': 'https://www.pngfind.com/pngs/m/606-6067999_professional-10-inch-full-range-karaoke-speaker-for.png',
                'category': categories['Party Equipment']
            },
            {
                'title': 'GoPro Hero 11 Black',
                'description': 'Action camera with 5.3K video, advanced stabilization, and waterproof housing. Ideal for extreme sports.',
                'price_per_day': 12.00,
                'image_url': 'https://carmarthencameras.com/cdn/shop/files/gopro-hero-11-black-pdp-h11b-SA-image02-1920-2x.webp?v=1736342495&width=1000',
                'category': categories['Electronics']
            },
            {
                'title': 'Aluminum Folding Ladder',
                'description': 'Versatile 4.5m multi-purpose folding ladder. Stable, lightweight, and easy to transport.',
                'price_per_day': 5.00,
                'image_url': 'https://images.unsplash.com/photo-1621905251918-48416bd8575a?w=800',
                'category': categories['Tools']
            }
        ]

        for item_data in items_data:
            if isinstance(item_data['category'], str):
                item_data['category'] = categories[item_data['category']]

            item, created = Item.objects.get_or_create(
                title=item_data['title'],
                defaults=item_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added item: {item.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Item already exists: {item.title}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))

