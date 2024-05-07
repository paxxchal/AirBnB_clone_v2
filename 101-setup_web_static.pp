class web_static {
  file { '/data':
    ensure => 'directory',
  }
  file { '/data/web_static':
    ensure => 'directory',
  }
  file { '/data/web_static/releases':
    ensure => 'directory',
  }
  file { '/data/web_static/shared':
    ensure => 'directory',
  }
  file { '/data/web_static/releases/test':
    ensure => 'directory',
  }
  file { '/data/web_static/releases/test/index.html':
    content => '<html><head><title>AirBnB clone</title></head><body><header></header><footer><p>Holberton School</p></footer></body></html>',
    ensure  => 'present',
  }
  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test',
  }
  package { 'nginx':
    ensure => 'present',
  }
  service { 'nginx':
    ensure  => 'running',
    enable  => 'true',
  }
  file { '/etc/nginx/sites-available/web_static':
    content => "
server {
    listen 80;
    server_name web_static;
    location / {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}
",
    ensure  => 'present',
  }
  file { '/etc/nginx/sites-enabled/web_static':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/web_static',
  }
}
