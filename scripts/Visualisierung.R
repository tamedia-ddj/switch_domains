#Clear workspace
rm(list = ls())
#Set working directory
setwd("~/Google Drive File Stream/Meine Ablage/Vorbereitung/20190225_Switch_Domains")
#Set preferred options
options(stringsAsFactors = FALSE)

#Load libraries
library(feather)
library(ggplot2)
library(tidyverse)

topurls.df <- data.frame(read_feather('data/all_data.feather'))

ggplot(data=topurls.df[10:1], aes(x=date, y=finarea.ch)) +
  geom_line() + geom_point()+
  scale_color_brewer(palette="Paired")+
  theme_minimal()

url_categories.df <- data.frame(read_feather('data/categories_viz.feather'))

ggplot(data=url_categories.df[url_categories.df$category != "Auctions" & url_categories.df$category != "SocialNetworking" & url_categories.df$category != "Audio/VideoClips",], aes(x = date, y=pageviews, group = category, colour=category)) +
  geom_line() +
  theme_minimal()
