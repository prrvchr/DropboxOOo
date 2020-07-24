#!
# -*- coding: utf-8 -*-

# Provider configuration
g_scheme = 'vnd.dropbox-apps'
g_extension = 'DropboxOOo'
g_identifier = 'com.gmail.prrvchr.extensions.%s' % g_extension
g_logger = '%s.Logger' % g_identifier

g_provider = 'Dropbox'
g_host = 'api.dropboxapi.com'
g_version = '2'
g_url = 'https://%s/%s' % (g_host, g_version)
g_upload = 'https://content.dropboxapi.com/2'

g_userfields = 'id,userPrincipalName,displayName'
g_drivefields = 'id,createdDateTime,lastModifiedDateTime,name'
g_itemfields = '%s,file,size,parentReference' % g_drivefields

# Minimun chunk: 327680 (320Ko) no more uploads if less... (must be a multiple of 64Ko (and 32Ko))
g_chunk = 327680  # Http request maximum data size, must be a multiple of 'g_length'
g_buffer = 32768  # InputStream (Downloader) maximum 'Buffers' size
g_pages = 100

g_office = 'application/vnd.oasis.opendocument'
g_folder = 'application/vnd.dropbox-apps.folder'
g_link = 'application/vnd.dropbox-apps.link'
g_doc_map = {'application/vnd.microsoft-apps.document':     'application/vnd.oasis.opendocument.text',
             'application/vnd.microsoft-apps.spreadsheet':  'application/x-vnd.oasis.opendocument.spreadsheet',
             'application/vnd.microsoft-apps.presentation': 'application/vnd.oasis.opendocument.presentation',
             'application/vnd.microsoft-apps.drawing':      'application/pdf'}

g_cache = 20
g_sync = 600
g_admin = False
