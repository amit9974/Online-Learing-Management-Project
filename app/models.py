from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
# Contact Form Model
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email



# Course Category Model
class CourseCategory(models.Model):
    icon = models.FileField(upload_to='Media/Course_Icon', null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name


# Author Model
class Author(models.Model):
    author_profile = models.ImageField(upload_to='Media/author')
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name



# Course List Model
class CourseList(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    
    image = models.ImageField(upload_to="Media/featured_img", null=True)
    video = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    description =models.TextField()
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='',max_length=500,null=True,blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    duration = models.CharField(max_length=50, null=True)
    lecture = models.IntegerField(null=True)
    enroll_course = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True)
    skill_level = models.CharField(max_length=50, null=True)
    certificate = models.CharField(max_length=4,null=True)
    what_you_learn = models.TextField(max_length=500, null=True)
    requirements = models.TextField(max_length=500, null=True)


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_details", kwargs={'slug': self.slug}) 


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = CourseList.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, CourseList)



class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
   

class Lesson(models.Model):
    course = models.ForeignKey(CourseList, on_delete=models.CASCADE, related_name='lesson_name')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.course.title



class Video(models.Model):
    serial_num = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to='Media/Ytb', null=True)
    course = models.ForeignKey(CourseList, on_delete=models.CASCADE, related_name='course_name')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_of_course')
    title = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=200)
    time_duration = models.FloatField(null=True)
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title

