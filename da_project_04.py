import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv') #, parse_dates=['date'], index_col= 'date')
df = df.drop('date,value', 1) #excel file column
# print(df.head())
df.set_index('date', drop=True, inplace=True)
# df.index.name = None #removes 'date' from first row of index column
# df.index = [pd.Timestamp(d) for d in df.index]

# print(df.head())

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]
print(df.head())
print(df.info())
print(df.count())


# fig = sns.lineplot(x='date', y='value', data=df) #.figure is matplotlib method
# fig = fig.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019').figure
# plt.xlabel('Date')
# plt.ylabel('Page Views')
# plt.xlim()
# plt.xticks([0, 200, 400, 600, 800, 1000, 1200, 1400],['2016-07', '2017-01', '2017-07', '2018-01', '2018-07', '2019-01', '2019-07', '2020-01'])
# # plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
# # plt.show(fig)
# fig.savefig('line_plot.png')

# df['datee'] = df.index #adding the date column back into the data
# # print(df.info())
# df['datee'] = pd.to_datetime(df['datee'])
# df['year'] = df['datee'].dt.year
# df['month'] = df['datee'].dt.month
# df['avg'] = df.groupby(['month', 'year']).value.mean()
# print(df.head())
# print(df.shape())

# df_bar = df.groupby(['month', 'year']).value.mean()
# print(df_bar)
#
# fig = sns.barplot(x='year', y='value', hue='month', data=df, ci=None).figure
# plt.xlabel('Years')
# plt.xticks(rotation=90)
# plt.ylabel('Average Page Views')
# plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],title='Months')
# plt.tight_layout() #fixes text from being cutoff in png
# fig.savefig('bar_plot.png')

# df_box = df.copy()
# df_box.reset_index(inplace=True)
# df_box['year'] = [d.year for d in df_box.date]
# df_box['month'] = [d.strftime('%b') for d in df_box.date]


# fig, ax = plt.subplots(1,2) # this means 1 figure(graph) on 2 axises (two graphs side by side)
# sns.boxplot(x='year', y='value', data=df, ax=ax[0])
# sns.boxplot(x='month', y='value', data=df, ax=ax[1])
# ax[0].set_xlabel('Year')
# ax[0].set_ylabel('Page Views')
# ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=10)
# ax[1].set_xlabel('Month')
# ax[1].set_ylabel('Page Views')
# ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=10)
# ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=6)
# plt.tight_layout()
# fig.savefig('box_plot.png')

def draw_line_plot():
    # Draw line plot
    fig = sns.lineplot(x='date', y='value', data=df) #.figure is matplotlib method
    fig = fig.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019').figure
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xlim()
    plt.xticks([0, 200, 400, 600, 800, 1000, 1200, 1400],['2016-07', '2017-01', '2017-07', '2018-01', '2018-07', '2019-01', '2019-07', '2020-01'])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # df_bar = df.groupby(['month', 'year']).value.mean()
    # Draw bar plot
    fig = sns.barplot(x='year', y='value', hue='month', data=df, ci=None).figure
    plt.xlabel('Years')
    plt.xticks(rotation=90)
    plt.ylabel('Average Page Views')
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2) # this means 1 figure(graph) on 2 axises (two graphs side by side)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=10)
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=10)
    ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=6)
    plt.tight_layout()





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
