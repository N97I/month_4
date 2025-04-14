from django.db import models


# """CREATE TABLE posts(id serial primary key autoincrement, title varchar(256), content varchar(856), rate int);"""


# """
# all objects - SELECT * FROM prost ==> Post.objects.all()

# fitltered objects - SELECT * FROM post WHERE  title ILIKE("title") ==> Post.objects.filter(title_icontains="title)

# one object - SELECT * FROM post WHERE id=1 ==> Post.objects.get(id=1)
# """
class Post(models.Model):
    title = models.CharField(max_length=356)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)



    def __str__(self):
        return f"{self.title} {self.content} {self.id}"



 