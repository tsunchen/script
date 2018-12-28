sed -i -E 's/external_url 'http:\/\/gitlab.example.com'/external_url 'http:\/\/localhost:25322/'  /etc/gitlab/gitlab.rb
sed -i -E 's/# nginx['listen_port'] = nil/nginx['listen_port'] = 25322/'  /etc/gitlab/gitlab.rb
