import { Avatar, Box,Card, CardContent, Grid, Typography } from '@mui/material';
import WaterIcon from '@mui/icons-material/Opacity';

export const TotalProfit = (props) => (
  <Card {...props}>
    <CardContent>
      <Grid
        container
        spacing={3}
        sx={{ justifyContent: 'space-between' }}
      >
        <Grid item>
          <Typography
            color="textSecondary"
            gutterBottom
            variant="overline"
          >
            TOTAL WATER SAVED
          </Typography>
          <Typography
            color="textPrimary"
            variant="h4"
          >
            2000 gal
          </Typography>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              backgroundColor: 'primary.main',
              height: 56,
              width: 56
            }}
          >
            <WaterIcon />
          </Avatar>
        </Grid>
      </Grid>
      <Box
        sx={{
          pt: 2,
          display: 'flex',
          alignItems: 'center'
        }}
      >
    
        <Typography
          color="textSecondary"
          variant="caption"
        >
          Since last quarter
        </Typography>
      </Box>
    </CardContent>
  </Card>
);
