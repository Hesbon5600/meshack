from django.shortcuts import render

from django.views.generic import TemplateView

from app.portfolio.models import Category, ExtraImage, Profile, Project, Service, Socials


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        projects = Project.objects.all()
        categories = Category.objects.all()
        socials = Socials.objects.all()
        profile = Profile.objects.first()
        services = Service.objects.all()
        extra_images = ExtraImage.objects.all()
        return render(request, self.template_name,
                      context={"projects": projects, "categories": categories,
                               'socials': socials, 'profile': profile,
                               'services': services, 'extra_images': extra_images})


class ProjectView(TemplateView):
    template_name = "project.html"

    def get(self, request, project_name):
        socials = Socials.objects.all()
        project = Project.objects.get(slug__iexact=project_name)
        return render(request, self.template_name, context={"project": project, 'socials': socials})


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        socials = Socials.objects.all()
        return render(request, self.template_name, context={"socials": socials})


class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        socials = Socials.objects.all()
        return render(request, self.template_name, context={"socials": socials})
