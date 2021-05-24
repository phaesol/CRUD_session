from django.shortcuts import render,redirect,get_object_or_404
from .models import Write,Comment,User
from .forms import WriteForm,CommentForm



def index(request):
    all_write = Write.objects.all()
    user = request.user
    
    return render(request,'index.html',{'all_write':all_write,'user':user})


def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    else:
        create_form = WriteForm()
    return render(request,'create.html',{'create_form':create_form})


def detail(request,write_id):
    list = []
    all_write = Write.objects.all()
    user = request.user
    my_write = get_object_or_404(Write,id=write_id)
    count = my_write.title
    print(my_write.title)
    for i in all_write:
        list.append(i.title)
       
    write_count = list.index(count)+1
    # print(list)
    # print(list.index(count)+1)

    comment_form = CommentForm()
    comments = Comment.objects.filter(post=write_id)
    
    return render(request,'detail.html',{'my_write':my_write,'all_write':all_write,'write_count':write_count,'comment_form':comment_form,'comments':comments,'user':user})

def update(request,write_id):
    my_write = get_object_or_404(Write,id=write_id) 
    if request.method == "POST": 
        update_form = WriteForm(request.POST,instance=my_write)
       
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    
    else:
        update_form = WriteForm(instance=my_write)
    return render(request,'update.html',{'update_form':update_form})


def delete(request,write_id):
    my_write = get_object_or_404(Write,id=write_id)
    my_write.delete()
    return redirect('index')
   

def create_comment(request,write_id):
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            form = comment.save(commit=False)
            user = request.user
            form.user = User.objects.get(id=user.id)
            form.post = Write.objects.get(id=write_id)
            form.save()
    return redirect('main:detail',write_id)


def delete_comment(request,write_id,comment_id):
    my_comment = get_object_or_404(Comment,id=comment_id)
    my_comment.delete()
    return redirect('main:detail',write_id)