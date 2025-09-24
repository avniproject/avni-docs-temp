title: Guide To Export and Import Reports across different Jasper Servers
excerpt: ''
## Reference: [https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-security-guide/vv900/jasperreports-server-security-guide-\_-keymanagement-\_-import\_and\_export/#Key\_Command\_Line\_Export](https://community.jaspersoft.com/documentation/jasperreports-server/tibco-jasperreports-server-security-guide/vv900/jasperreports-server-security-guide-_-keymanagement-_-import_and_export/#Key_Command_Line_Export)

## Login into Source server

## Execute below commands to export the report

```
## Navigate to scripts dir
cd /home/ubuntu/jasperreports-server-cp-7.5.0-bin/buildomatic  
## Execute the report export script
./js-export.sh --uris /RWB_2023 --output-zip gramin_rwb_2023.zip --secret-key="\<specify_key_value>"  
## Copy the generated export file to home dir
cp gramin_rwb_2023.zip ~/  
## Exit
exit
```

## Transfer file to your system using scp

Ex: from your machine terminal

```shell Shell
scp jasper-reporting-openchs:gramin_rwb_2023.zip ./
```

## Login into Target Jasper server webapp

Import the zip file in target jasper using the "Key Value" option by specifying the key value "\<specify\_key\_value>" used during export.

<Image align="center" src="https://files.readme.io/6ca70fd-Screenshot_2024-03-15_at_4.32.26_PM.png" />
