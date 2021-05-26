from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, FormView, UpdateView

from .forms import CommentForm, CreatepostForm, ModifpostForm
from .models import *
from . import forms


# Create your views here.


def login_view(request):
    error = False

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                error = True
    else:
        form = forms.LoginForm()
    return render(request, 'registration/login.html', locals())


@login_required
def logout_view(request, **kwargs):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


class communautes(LoginRequiredMixin, ListView):
    template_name = 'communautes.html'
    model = Communautes
    context_object_name = "communautes"

    def post(self, request):
        user = request.user
        if request.method == 'POST':
            abn = request.POST.get('abn_stat')
            comm = get_object_or_404(Communautes, pk=request.POST.get('communaute'))
            if abn == 'on':
                comm.abonnes.remove(user)
            elif abn == 'off':
                comm.abonnes.add(user)
            return render(request, self.template_name, {'communautes': Communautes.objects.all()})


class communaute(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'communaute.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(communaute=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(communaute, self).get_context_data(**kwargs)
        context['commmunaute'] = Communautes.objects.get(pk=self.kwargs['pk'])
        return context


class post(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(post, self).get_context_data(**kwargs)
        context['commentaires'] = Commentaire.objects.filter(post=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.auteur = self.request.user
        comment.post = Post.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return super(post, self).form_valid(form)


class nouveau_post(LoginRequiredMixin, CreateView):
    template_name = 'post-create.html'
    form_class = CreatepostForm
    model = Post

    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(nouveau_post, self).get_context_data(**kwargs)
        context['communautes'] = Communautes.objects.all()
        context['priorites'] = Priorite.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auteur = self.request.user
            comment.save()
        return super().form_valid(form)


class modif_post(LoginRequiredMixin, UpdateView):
    template_name = 'modif-post.html'
    form_class = ModifpostForm

    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        code = self.kwargs.get('pk', None)
        return get_object_or_404(Post, pk=code)


class all_post(LoginRequiredMixin, ListView):
    template_name = 'post-all.html'
    context_object_name = 'posts'
    model = Post
