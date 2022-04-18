from django.shortcuts import render

from django.views.generic import TemplateView

from app.portfolio.models import Category, Project, Socials


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        projects = Project.objects.filter(deleted=False).all()
        categories = Category.objects.filter(deleted=False).all()
        socials = Socials.objects.filter(deleted=False).all()
        return render(request, self.template_name, context={"projects": projects, "categories": categories, 'socials': socials})


class ProjectView(TemplateView):
    template_name = "project.html"

    def get(self, request, project_name):
        socials = Socials.objects.filter(deleted=False).all()
        project = Project.objects.get(slug__iexact=project_name)
        return render(request, self.template_name, context={"project": project, 'socials': socials})


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        socials = Socials.objects.filter(deleted=False).all()
        return render(request, self.template_name, context={"socials": socials})


class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        socials = Socials.objects.filter(deleted=False).all()
        return render(request, self.template_name, context={"socials": socials})
