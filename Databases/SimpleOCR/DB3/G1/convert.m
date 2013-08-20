
filesystem = dir;
%nomes = ;

for i=1:length(filesystem)
    arquivo = filesystem(i).name;
    if strfind(arquivo,'.png')>0
        im = imread(arquivo);
        im2 = imresize(im,16/22);
        imb = im2bw(im2,0.6)';
        arquivo(length(arquivo) ) ='t';
        arquivo(length(arquivo) -1) ='x';
        arquivo(length(arquivo) -2) ='t';
        fid = fopen(arquivo,'w');
        fprintf(fid,'%d ',imb);
        fclose(fid);
    end
end
