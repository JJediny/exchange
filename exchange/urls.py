# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 Boundless Spatial
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from maploom.geonode.urls import urlpatterns as maploom_urls
from hypermap.urls import urlpatterns as hypermap_urls
from osgeo_importer.urls import urlpatterns as osgeo_importer_urls
from osgeo_importer.views import FileAddView
from geonode.urls import urlpatterns as geonode_urls
from . import views

js_info_dict = {
    'packages': ('geonode.layers',),
}

urlpatterns = patterns(
    '',
    url(r'^/?$', views.HomeScreen, name='home'),
    url(r'^layers/(?P<layername>[^/]*)/metadata_detail$',
        views.layer_metadata_detail, name='layer_metadata_detail'),
    url(r'^maps/(?P<mapid>[^/]*)/metadata_detail$', views.map_metadata_detail,
        name='map_metadata_detail'),
    url(r'^wfsproxy/', views.geoserver_reverse_proxy,
            name='geoserver_reverse_proxy')
 )


if 'osgeo_importer' in settings.INSTALLED_APPS:
    # if using osgeo_importer, intercept the usual layers/upload view in order
    # to use alternate UI (from django_osgeo_importer)
    urlpatterns += [url(r'^layers/upload$',
                        login_required(FileAddView.as_view()),
                        name='layer_upload')]
    urlpatterns += osgeo_importer_urls

urlpatterns += geonode_urls
urlpatterns += maploom_urls
urlpatterns += hypermap_urls
